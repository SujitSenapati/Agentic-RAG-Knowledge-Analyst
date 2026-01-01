"""
Gradio-based user interface for the Agentic RAG system.

Responsibilities:
- Provide a simple interactive UI for testing the agent
- Forward user questions to the agent execution loop
- Display the final answer and agent trace for auditability
- Contain NO business, planning, or retrieval logic
"""

import gradio as gr
from typing import Tuple, Dict, Any
from app.agent.agent_loop import run_agent


def ask(question: str):
    """
    Handle a user question submitted from the UI.

    Args:
        question (str): Natural language question entered by the user

    Returns:
        Tuple:
            - str: Final agent answer or clarification question
            - Dict: Agent execution trace (plan, tools used)
    """
    answer, trace = run_agent(question)
    return answer, trace


def launch():
    """
    Launch the Gradio application.

    UI Components:
    - Textbox for user questions
    - Markdown panel for the agent answer
    - JSON panel for agent trace (planner output, tools used)
    """
    with gr.Blocks() as demo:
        gr.Markdown("# Agentic RAG – Enterprise Knowledge Analyst")

        question = gr.Textbox(
            label="Question",
            placeholder="Ask about Kubernetes, incidents, compliance, or APIs..."
        )

        askQns = gr.Button("Ask Agent")

        answer = gr.Markdown(label="Answer")
        trace = gr.JSON(label="Agent Trace")

        askQns.click(
            ask,
            inputs=question,
            outputs=[answer, trace]
        )

    demo.launch()
