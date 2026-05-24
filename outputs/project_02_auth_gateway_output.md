# Project 02 Auth Gateway Output

## Command Run

```bash
curl -X POST http://localhost:8000/auth/login
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
{"access_token":"eyJ...demo","token_type":"bearer","role":"customer"}
```

## Explanation

Mock OAuth/JWT and role claims work.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
