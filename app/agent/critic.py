"""
Critic module.

Performs a lightweight logical consistency check on the agent's answer
before final evaluation by the judge.
"""

import json
from app.llms import llm_fast
from app.utils import load_prompt


def critique_answer(question: str, answer: str, evidence: str) -> dict:
    """
    Critique the agent's answer for logical consistency and alignment.

    Args:
        question (str): Original user question
        answer (str): Agent-generated answer
        evidence (str): Evidence used during reasoning

    Returns:
        dict: Critic feedback with needs_revision flag and rationale
    """

    # Load the critic prompt template
    template = load_prompt("critic.txt")

    # 🔑 Inject question, answer, and evidence into the prompt
    prompt = template.format(
        question=question,
        answer=answer,
        evidence=evidence
    )

    # Invoke LLM
    response = llm_fast.invoke(prompt).content.strip()

    # Parse strict JSON
    return json.loads(response)
