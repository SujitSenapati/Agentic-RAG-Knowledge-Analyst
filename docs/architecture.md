# System Architecture

This document describes the **end-to-end architecture** of the Agentic RAG – Enterprise Knowledge Analyst system.

The system is intentionally split into **two distinct phases**:

1. **Offline Ingestion Phase** – deterministic data preparation
2. **Online Agent Runtime Phase** – dynamic agent reasoning

---

## High-Level Architecture Overview
```mermaid

flowchart TD

  %% ------------------------
  %% Offline Ingestion Phase
  %% ------------------------
  subgraph Offline["Offline Ingestion Phase"]
      U1[Public Documentation URLs]
      U1 --> F[Fetch & Clean Content]
      F --> C[Chunking]
      C --> E[Embedding]
      E --> VS[(Persistent Vector Stores)]
  end

  %% ------------------------
  %% Online Agent Runtime
  %% ------------------------
  subgraph Online["Online Agent Runtime"]

      User[User] --> UI[Gradio UI]
      UI --> A[Agent Loop]

      A --> P[Planner]
      P -->|Intent, Tools, Clarification| A

      A --> TR[Tool Registry]

      TR --> T1[Kubernetes Docs Tool]
      TR --> T2[Incident Reports Tool]
      TR --> T3[Policy / GDPR Tool]
      TR --> T4[StackOverflow Tool]
      TR --> T5[OpenAI API Docs Tool]
      TR --> T6[GitHub Issues Tool]

      T1 --> VS
      T2 --> VS
      T3 --> VS
      T4 --> VS
      T5 --> VS
      T6 --> VS

      VS --> EV[Evidence Builder]
      EV --> RS[Reasoner]
      RS --> ANS[Draft Answer]

      ANS --> C[Critic]
      C -->|Refine if needed| RS

      RS --> J[LLM Judge]
      J -->|Approve| UI
      J -->|Retry Once| RS

      A -. traces .-> LS[LangSmith Tracing]
  end
```