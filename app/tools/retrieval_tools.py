"""
Vector-based retrieval tools.

Responsibilities:
- Wrap each vector store as a self-describing tool
- Expose retrieval capability without routing logic
"""

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.config import VECTORSTORE_DIR
from app.tools.registry import register_tool

emb = OpenAIEmbeddings(model="text-embedding-3-small")

vs_k8s = Chroma(
    persist_directory=f"{VECTORSTORE_DIR}/k8s",
    embedding_function=emb,
    collection_name="k8s"
)

vs_incidents = Chroma(
    persist_directory=f"{VECTORSTORE_DIR}/incidents",
    embedding_function=emb,
    collection_name="incidents"
)

vs_policy = Chroma(
    persist_directory=f"{VECTORSTORE_DIR}/policy",
    embedding_function=emb,
    collection_name="policy"
)

vs_stackoverflow = Chroma(
    persist_directory=f"{VECTORSTORE_DIR}/stackoverflow",
    embedding_function=emb,
    collection_name="stackoverflow"
)


@register_tool(
    name="search_kubernetes_docs",
    description="Kubernetes concepts, RBAC, workloads, networking, cluster operations.",
    domains=["kubernetes", "rbac", "k8s"]
)
def search_kubernetes_docs(query: str):
    """Search Kubernetes documentation."""
    return vs_k8s.similarity_search(query, k=6)


@register_tool(
    name="search_incident_reports",
    description="Outages, postmortems, reliability incidents, root cause analysis.",
    domains=["incident", "outage", "postmortem"]
)
def search_incident_reports(query: str):
    """Search incident reports."""
    return vs_incidents.similarity_search(query, k=6)


@register_tool(
    name="search_policy_docs",
    description="GDPR, privacy, compliance, regulatory requirements.",
    domains=["gdpr", "compliance", "policy"]
)
def search_policy_docs(query: str):
    """Search policy documents."""
    return vs_policy.similarity_search(query, k=6)

@register_tool(
    name="search_stackoverflow",
    description="Community Q&A for debugging, errors, and practical solutions.",
    domains=["stackoverflow", "error", "debugging"]
)
def search_stackoverflow(query: str):
    """Search StackOverflow posts."""
    return vs_stackoverflow.similarity_search(query, k=6)
