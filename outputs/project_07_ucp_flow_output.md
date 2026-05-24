# Project 07 Ucp Flow Output

## Command Run

```bash
cd ucp-flow && python sample_ucp_flow.py
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
{"step":5,"name":"cart_mandate_creation","payload":{"budget_limit":40}}
```

## Explanation

UCP-style local mandate flow is visible.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
