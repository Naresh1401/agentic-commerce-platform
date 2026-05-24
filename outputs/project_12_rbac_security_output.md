# Project 12 Rbac Security Output

## Command Run

```bash
curl http://localhost:8000/security/demo?role=partner_agent
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
{"allowed_actions":[{"action":"create_checkout_session","allowed":false}]}
```

## Explanation

RBAC and PII masking are visible.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
