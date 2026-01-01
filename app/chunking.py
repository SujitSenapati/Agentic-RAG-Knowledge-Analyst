"""
Text chunking utilities.

This module provides a configured `RecursiveCharacterTextSplitter`
used by the ingestion pipeline to split large documents into
appropriately sized chunks for embedding and retrieval.

Configuration notes:
- `chunk_size` controls the maximum tokens/characters per chunk.
- `chunk_overlap` enables context overlap between contiguous chunks
    to preserve continuity for retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=150
)
