# System Architecture

This document describes the **end-to-end architecture** of the Agentic RAG – Enterprise Knowledge Analyst system.

The system is intentionally split into **two distinct phases**:

1. **Offline Ingestion Phase** – deterministic data preparation
2. **Online Agent Runtime Phase** – dynamic agent reasoning

---
## 1. Original Agentic RAG Architecture (Conceptual Core)

This conceptual architecture **remains valid** and continues to guide the implementation.

```mermaid
flowchart TD
  U[User] --> UI[Gradio UI]
  UI --> A[Agent Loop]

  A --> P[Planner]
  P -->|plan: intent, tools, clarification| A

  A --> TE[Tool Executor]
  TE --> R1[K8s Docs]
  TE --> R2[Incidents]
  TE --> R3[Policy]

  R1 --> EV[Evidence]
  R2 --> EV
  R3 --> EV

  EV --> RS[Reasoner]
  RS --> ANS[Draft Answer]

  ANS --> C[Critic]
  C -->|Refine if needed| RS

  RS --> J[LLM Judge]
  J -->|Approve| UI
  J -->|Retry once| RS

  A -. traces .-> LS[LangSmith]
```

---

## 2. Final Architecture (Full System View)

The final system **extends** the original design with:

* Offline ingestion
* Persistent vector stores
* Capability-based tools
* Tool registry
* Multi-layer answer verification
* Controlled auto-retry

```mermaid
flowchart LR

  %% ------------------------
  %% Offline Ingestion Phase
  %% ------------------------
  subgraph Offline["Offline Ingestion Phase"]
      U1[Public URLs] --> F[Fetch & Clean HTML]
      F --> C[Chunking]
      C --> E[Embedding]
      E --> VS[(Persistent Vector Stores)]
  end

  %% ------------------------
  %% Online Runtime Phase
  %% ------------------------
  subgraph Online["Online Agent Runtime"]

      User[User] --> UI[Gradio UI]
      UI --> A[Agent Loop]

      A --> P[Planner]
      P -->|Select tools| TR[Tool Registry]

      TR --> T1[Tool: Kubernetes Docs]
      TR --> T2[Tool: Incident Reports]
      TR --> T3[Tool: Policy / GDPR]
      TR --> T4[Tool: StackOverflow]
      TR --> T5[Tool: OpenAI API Docs]
      TR --> T6[Tool: GitHub Issues]

      T1 --> VS
      T2 --> VS
      T3 --> VS
      T4 --> VS
      T5 --> VS
      T6 --> VS

      VS --> EV[Evidence Builder]
      EV --> RS[Reasoner]
      RS --> ANS[Grounded Answer + Citations]

      ANS --> C[Critic / Verifier]
      C -->|OK| UI
      C -->|Retry / Refine| A

      A -. traces .-> LS[LangSmith Tracing]
  end
```