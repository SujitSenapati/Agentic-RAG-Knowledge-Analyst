"""
Agent execution loop.

Orchestrates:
- Planning
- Clarification
- Retrieval
- Reasoning
- Critique
- Judge evaluation
- Judge-based auto-retry
"""

from typing import Tuple, Dict, Any
from app.agent.planner import create_plan
from app.agent.reasoner import reason
from app.agent.critic import critique_answer
from app.agent.judge import judge_answer
from app.tools.evidence import retrieve_and_build_evidence
from app.utils import load_prompt
from app.llms import llm_fast


def run_agent(question: str):
    """
    Run the full agent loop.

    Args:
        question (str): User question

    Returns:
        Tuple[str, Dict]: Final answer and agent trace
    """

    # =========================
    # Initialize trace
    # =========================
    trace = {
        "question": question
    }

    # =========================
    # Planning
    # =========================
    plan = create_plan(question)

    trace["plan"] = {
        "intent": plan.intent,
        "subquestions": plan.subquestions,
        "tools": plan.tools,
        "need_clarification": plan.need_clarification,
        "clarification_question": plan.clarification_question,
    }

    print(trace["plan"])

    # =========================
    # Clarification path
    # =========================
    if plan.need_clarification:
        trace["final_state"] = "clarification"
        return plan.clarification_question, trace

    # =========================
    # Retrieval
    # =========================
    evidence = retrieve_and_build_evidence(
        tools=plan.tools,
        query=question
    )

    trace["evidence_size"] = len(evidence)

    # =========================
    # Reasoning
    # =========================
    answer = reason(question, evidence)

    # =========================
    # Critic (logical sanity check)
    # =========================
    critic_feedback = critique_answer(
        question=question,
        answer=answer,
        evidence=evidence
    )

    trace["critic"] = critic_feedback

    # If critic flags a hard failure, refine once
    if critic_feedback.get("needs_revision"):
        trace["critic_revision"] = True

        answer = reason(
            question,
            evidence,
            critique=critic_feedback.get("rationale")
        )

    # =========================
    # Judge (quality evaluator)
    # =========================
    judge = judge_answer(
        question=question,
        answer=answer,
        evidence=evidence
    )

    trace["judge"] = judge

    # =========================
    # Judge-based auto-retry (ONE TIME)
    # =========================
    if judge["verdict"] == "needs_review":
        trace["auto_retry"] = True

        retry_prompt = load_prompt("reasoner_retry.txt").format(
            question=question,
            answer=answer,
            judge_rationale=judge["rationale"],
            evidence=evidence
        )

        revised_answer = llm_fast.invoke(retry_prompt).content.strip()

        retry_judge = judge_answer(
            question=question,
            answer=revised_answer,
            evidence=evidence
        )

        trace["retry"] = {
            "judge": retry_judge
        }

        # Accept retry only if it improves quality
        if retry_judge["score"] >= judge["score"]:
            answer = revised_answer
            trace["judge"] = retry_judge

    # =========================
    # Finalize
    # =========================
    trace["final_state"] = "answered"
    return answer, trace
