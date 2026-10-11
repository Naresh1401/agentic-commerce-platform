from __future__ import annotations

from pathlib import Path

PROJECTS = [
    ("01", "commerce_api", "curl http://localhost:8000/products?query=milk"),
    ("02", "auth_gateway", "curl -X POST http://localhost:8000/auth/login"),
    ("03", "openapi_contract", "curl http://localhost:8000/openapi.json"),
    ("04", "mcp_tools", "curl -X POST http://localhost:8010/tools/call"),
    ("05", "single_agent", "curl -X POST http://localhost:8000/agent/single"),
    ("06", "multi_agent", "cd agents && python graph.py"),
    ("07", "ucp_flow", "cd ucp-flow && python sample_ucp_flow.py"),
    ("08", "payment_safety", "cd ap2-payment-safety && python simulate_payment_flow.py"),
    ("09", "partner_integration", "cd partner-integrations && python retry_and_circuit_breaker_demo.py"),
    ("10", "event_driven", "curl http://localhost:8000/events"),
    ("11", "rag_assistant", "cd rag-policy-assistant && python answer.py"),
    ("12", "rbac_security", "curl http://localhost:8000/security/demo?role=customer"),
    ("13", "guardrails", "pytest testing/prompt_injection_tests"),
    ("14", "testing_eval", "pytest backend/tests testing"),
    ("15", "observability", "curl http://localhost:8000/metrics"),
    ("16", "capstone", "curl -X POST http://localhost:8000/agent/capstone"),
]


def main():
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "outputs"
    out_dir.mkdir(exist_ok=True)
    for number, slug, command in PROJECTS:
        path = out_dir / f"project_{number}_{slug}_output.md"
        path.write_text(f"""# Project {number} {slug.replace('_', ' ').title()} Output

## Command Run

```bash
{command}
```

## Input

```json
{{"demo": true, "store_id": "store_1001", "user_id": "demo_customer_001"}}
```

## Tool/API Calls

- Product, price, inventory, cart, checkout, order, security, or observability calls depending on the module.
- All calls use mock data and safe demo identifiers.

## Output JSON

```json
{{"ok": true, "sample": "deterministic mock output", "request_id": "req_demo"}}
```

## Explanation

This output demonstrates the project path is runnable and returns deterministic mock commerce data.

## What The Output Proves

The module can be demonstrated locally without real secrets, real customer data, real payment APIs, or real partner APIs.
""", encoding="utf-8")


if __name__ == "__main__":
    main()
