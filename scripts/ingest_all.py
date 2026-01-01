"""
Offline ingestion runner.

Run this whenever you:
- Add new URLs
- Update documentation sources
- Refresh embeddings
"""

from app.ingestion import build_vectorstore
from app.utils import load_urls

print("Starting ingestion...")

build_vectorstore(
    urls=load_urls("data/urls_k8s.txt"),
    collection="k8s",
    source_type="techdoc",
    source_name="kubernetes"
)

build_vectorstore(
    urls=load_urls("data/urls_incidents.txt"),
    collection="incidents",
    source_type="incident",
    source_name="postmortems"
)

build_vectorstore(
    urls=load_urls("data/urls_policy.txt"),
    collection="policy",
    source_type="policy",
    source_name="gdpr"
)

build_vectorstore(
    urls=load_urls("data/urls_stackoverflow.txt"),
    collection="stackoverflow",
    source_type="stackoverflow",
    source_name="stackoverflow"
)

print("Ingestion completed successfully.")