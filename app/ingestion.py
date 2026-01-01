"""
Document ingestion and vector store construction.

Responsibilities:
- Fetch content from external URLs
- Clean and normalize raw HTML into text
- Chunk text into semantically searchable units
- Attach metadata for traceability and auditing
- Build and persist vector stores for retrieval tools

This module is executed during setup / preprocessing,
not during live agent execution.
"""

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.chunking import splitter
from app.config import VECTORSTORE_DIR

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def fetch_text(url: str) -> str:
    """
    Fetch and clean text content from a web URL.

    - Uses a browser-like User-Agent to avoid 403s
    - Fails gracefully if a page cannot be fetched
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=60)
        response.raise_for_status()
    except Exception as e:
        print(f"[WARN] Skipping URL due to fetch error: {url}")
        print(f"       Reason: {e}")
        return ""   # <---- critical: do NOT crash ingestion

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    return "\n".join(
        line.strip()
        for line in soup.get_text("\n").splitlines()
        if line.strip()
    )



def build_vectorstore(
    urls: list[str],
    collection: str,
    source_type: str,
    source_name: str
):
    """
    Build and persist a vector store from a list of URLs.

    For each URL:
    - Fetch text
    - Split into chunks
    - Attach metadata
    - Embed and store in Chroma

    Metadata fields:
    - url: original source URL
    - chunk_id: chunk index within the document
    - source_type: high-level category (techdoc, incident, policy)
    - source_name: logical dataset name

    Args:
        urls (list[str]): List of source URLs
        collection (str): Vector store collection name
        source_type (str): Category of source
        source_name (str): Human-readable source name

    Returns:
        Chroma: Persisted vector store instance
    """
    documents = []

    for url in urls:
        text = fetch_text(url)
        chunks = splitter.split_text(text)

        for i, chunk in enumerate(chunks):
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "url": url,
                        "chunk_id": i,
                        "source_type": source_type,
                        "source_name": source_name
                    }
                )
            )

    return Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=f"{VECTORSTORE_DIR}/{collection}",
        collection_name=collection
    )
