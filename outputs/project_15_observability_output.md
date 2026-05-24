# Project 15 Observability Output

## Command Run

```bash
curl http://localhost:8000/metrics
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
{"request_count":42,"avg_api_latency_ms":18.4,"tool_call_success_rate":98.2}
```

## Explanation

Metrics support the dashboard.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
