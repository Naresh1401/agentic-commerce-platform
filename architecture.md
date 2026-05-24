# Architecture

The platform is split into demo-friendly layers:

- Frontend layer: React pages for APIs, agents, UCP, payment safety, partners, RAG, security, testing, observability, and architecture.
- Commerce API layer: FastAPI routers for products, inventory, pricing, coupons, cart, checkout, orders, partners, auth, health, metrics, traces, and event replay.
- Security layer: mock OAuth login, JWT-like claims, partner API keys, RBAC, row-level access, guardrails, and PII masking.
- Orchestration layer: response normalization, retry policy, circuit breaker, and capstone workflow.
- MCP layer: lightweight JSON tool server that validates schemas and enforces tool permissions.
- Agent layer: single-agent and multi-agent workflow with shared state and deterministic mock LLM routing.
- UCP-style layer: merchant capability discovery, cart mandate, checkout hydration, confirmation, and order tracking.
- AP2-style layer: payment mandate simulation, audit log, idempotency, success, duplicate, and decline paths.
- RAG layer: local markdown policies with deterministic retrieval and grounded citations.
- Observability layer: JSON logs, request IDs, traces, metrics, event timeline, and frontend dashboard.
- Testing layer: API, integration, contract, MCP schema, golden dataset, prompt injection, RBAC, and RAG tests.
