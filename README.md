    # Agentic Commerce Platform

    A complete GitHub-ready training monorepo for an **Agentic AI API Developer - Agentic Commerce & Third-Party Integrations** role. It is a Kroger-style grocery commerce platform built entirely with mock data, mock payments, mock partner integrations, and deterministic agent behavior by default.

    No real Kroger APIs, real payment APIs, real customer data, or real secrets are used.

    ## Architecture

    ```mermaid
    flowchart LR
      UI[React Demo UI] --> API[FastAPI Commerce APIs]
      UI --> Agents[Single + Multi-Agent Workflows]
      Agents --> MCP[MCP-Style Tool Server]
      MCP --> API
      Partners[Fake Partner A/B] --> Adapter[Partner Adapter]
      Adapter --> API
      API --> Events[Event Bus]
      API --> Metrics[Metrics + Traces]
      RAG[RAG Policy Assistant] --> Policies[Local Markdown Policies]
      Checkout[Checkout] --> AP2[AP2-Style Payment Safety]
      UCP[UCP-Style Flow] --> API
    ```

    ## Tech Stack

    - Backend: Python 3.11+, FastAPI, Pydantic, SQLAlchemy, PostgreSQL-ready, Redis-ready, Uvicorn
    - Agents: deterministic mock LLM by default, LangGraph-ready structure
    - MCP: lightweight MCP-style JSON tool server
    - Frontend: React, Vite, TypeScript, Tailwind CSS
    - RAG: deterministic local retrieval over markdown policy files
    - Testing: pytest, HTTPX/TestClient, contract tests, golden datasets, prompt injection tests
    - DevOps: Docker, Docker Compose, Makefile, GitHub Actions

    ## Quick Start

    ```bash
    docker compose up --build
    ```

    Frontend: http://localhost:5173  
    Backend Swagger: http://localhost:8000/docs  
    Metrics: http://localhost:8000/metrics  
    MCP server: http://localhost:8010/tools/list

    ## Local Run

    ```bash
    cd backend
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8000
    ```

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

    ```bash
    cd mcp-server
    pip install -r requirements.txt
    python server.py
    ```

    ```bash
    cd agents
    pip install -r requirements.txt
    python graph.py
    ```

    ## Run Tests

    ```bash
    make test
    make test-contract
    make test-agents
    ```

    ## Projects

    01. **Commerce REST API Backend** - FastAPI catalog, inventory, pricing, carts, checkout, orders, health, and metrics.
02. **API Gateway + Authentication** - Mock OAuth2/JWT, partner API keys, RBAC, audit logs, PII masking, request IDs.
03. **OpenAPI + Contract Testing** - Swagger/OpenAPI contracts with schema and compatibility tests.
04. **MCP Server for Commerce Tools** - MCP-style JSON tool server for commerce operations with role-aware risk controls.
05. **Single Shopping Agent** - Deterministic shopping agent that calls tools and requires confirmation gates.
06. **Multi-Agent Commerce System** - Supervisor-routed product, pricing, inventory, cart, coupon, checkout, and order agents.
07. **UCP-Style Agentic Commerce Flow** - Local UCP-style capability discovery, cart mandate, and checkout hydration demo.
08. **AP2-Style Payment Safety Simulation** - Mock payment mandates, idempotency, audit trail, declines, and success paths.
09. **Partner Integration Adapter** - Partner A/B schema transforms, retries, circuit breaker, DLQ, and error mapping.
10. **Event-Driven Commerce** - In-memory event bus with producers, consumers, event log endpoint, and replay.
11. **RAG Assistant for Commerce Policies** - Deterministic policy retrieval over local markdown with grounded answers and citations.
12. **RBAC and Data Security** - Role claims, row-level order access, PII masking, and tool permission checks.
13. **Agent Guardrails and Negative Tests** - Prompt injection, unauthorized payment, hallucination, PII, and coupon abuse defenses.
14. **Agentic Testing and Evaluation** - Golden dataset and API, MCP, RAG, RBAC, latency, and safety test framework.
15. **Observability Dashboard** - Metrics, traces, structured logs, and frontend dashboard.
16. **End-to-End Capstone Demo** - Pasta dinner workflow from intent to mandate, order, events, and tracking.

    ## Interview/Kickoff Talking Points

    - This is API-first: FastAPI owns OpenAPI and contract tests protect key payloads.
    - Agents do not invent deterministic commerce facts; they call tools for price, inventory, orders, and coupons.
    - MCP-style tools are role-aware and risk-classified.
    - UCP-style and AP2-style demos are clearly labeled as local simulations, not official certified implementations.
    - Guardrails cover prompt injection, unauthorized payment, hallucinated products, coupon abuse, and PII masking.
    - Observability is visible in `/metrics`, `/traces`, event logs, and the frontend dashboard.
