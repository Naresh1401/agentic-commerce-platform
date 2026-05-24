# Project 03 Openapi Contract Output

## Command Run

```bash
curl http://localhost:8000/openapi.json
```

## Input

```json
{"store_id":"store_1001","user_id":"demo_customer_001","mock_only":true}
```

## Tool/API Calls

- Uses the local backend, MCP-style tools, or module script.
- Calls use mock grocery catalog, inventory, coupons, carts, orders, and demo roles.

## Output JSON

```json
{"openapi":"3.1.0","info":{"title":"Agentic Commerce Platform"}}
```

## Explanation

OpenAPI is generated for contract tests.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
