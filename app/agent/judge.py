"""
LLM-as-Judge module.

Evaluates the quality of the agent's final answer
based on grounding, relevance, and citation quality.
"""

import json
from app.llms import llm_fast
from app.utils import load_prompt


def judge_answer(question: str, answer: str, evidence: str) -> dict:
    """
    Evaluate the agent's answer using an LLM judge.

    Args:
        question (str): Original user question
        answer (str): Agent-generated answer
        evidence (str): Evidence used for reasoning

    Returns:
        dict: Structured evaluation verdict
    """
    prompt = load_prompt("judge.txt").format(
        question=question,
        answer=answer,
        evidence=evidence
    )

    response = llm_fast.invoke(prompt).content.strip()
    return json.loads(response)
