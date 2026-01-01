"""
Evidence construction utilities.

Responsibilities:
- Deduplicate retrieved documents
- Limit the amount of evidence passed to the LLM
- Format evidence with citations for traceability
- Provide a consistent, auditable evidence block

This module does NOT perform reasoning or retrieval.
"""
from app.tools.registry import TOOL_REGISTRY

def build_evidence(docs, limit: int = 15) -> str:
    """
    Build a formatted evidence block from retrieved documents.

    Each evidence entry includes:
    - Source name
    - Chunk ID
    - Source URL
    - Truncated content snippet

    Args:
        docs (list[Document]): Retrieved LangChain documents
        limit (int): Maximum number of evidence entries

    Returns:
        str: Formatted evidence text
    """
    seen = set()
    evidence_blocks = []

    for doc in docs:
        key = (doc.metadata["url"], doc.metadata["chunk_id"])

        if key in seen:
            continue

        seen.add(key)

        evidence_blocks.append(
            f"[{doc.metadata['source_name']}|{doc.metadata['chunk_id']}]"
            f"({doc.metadata['url']})\n"
            f"{doc.page_content[:400]}"
        )

        if len(evidence_blocks) >= limit:
            break

    return "\n\n".join(evidence_blocks)

def retrieve_and_build_evidence(
    tools: list,
    query: str,
    limit: int = 15
) -> str:
    """
    Retrieve documents using selected tools and build formatted evidence.

    Args:
        tools (list): List of tool names selected by the planner
        query (str): User question
        limit (int): Maximum number of evidence entries

    Returns:
        str: Formatted evidence text
    """
    all_docs = []

    for tool_name in tools:
        tool = TOOL_REGISTRY.get(tool_name)
        if not tool:
            continue

        docs = tool["func"](query)
        all_docs.extend(docs)

    return build_evidence(all_docs, limit=limit)