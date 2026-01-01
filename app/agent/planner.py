"""
Planner agent.

Responsibilities:
- Interpret user intent
- Select which tools to invoke
- Decide whether clarification is required
"""

import json
from pydantic import BaseModel
from typing import List, Optional
from app.llms import llm_fast
from app.tools.registry import TOOL_REGISTRY
from app.utils import load_prompt


class Plan(BaseModel):
    intent: str
    subquestions: List[str]
    tools: List[str]
    need_clarification: bool
    clarification_question: Optional[str]


def create_plan(question: str) -> Plan:
    """
    Generate a structured execution plan from the user question.
    """
    
    tools_desc = "\n".join(
        f"- {name}: {meta['description']}"
        for name, meta in TOOL_REGISTRY.items()
    )

    prompt = load_prompt("planner.txt").format(
        question=question,
        tools=tools_desc
    )

    response = llm_fast.invoke(prompt).content
    return Plan(**json.loads(response))
