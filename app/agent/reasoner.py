"""
Reasoning module for generating answers based on evidence.

Responsibilities:
- Formulate prompts combining questions and evidence
- Invoke LLM for reasoning
"""
from app.llms import llm_reasoning
from app.utils import load_prompt

def reason(question: str, evidence: str, critique: str | None = None) -> str:
    """
    Generate a reasoned answer based on the question and accumulated evidence.
    """
    prompt = load_prompt("reasoner.txt").format(
        question=question,
        evidence=evidence,
        critique=critique or "None"
    )
    return llm_reasoning.invoke(prompt).content
