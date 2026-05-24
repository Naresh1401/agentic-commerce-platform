# Project 16 Capstone Output

## Command Run

```bash
curl -X POST http://localhost:8000/agent/capstone
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
{"intent":"meal_planning_cart_checkout","budget_ok":true,"requires_confirmation":true}
```

## Explanation

End-to-end capstone prepares cart and checkout with confirmation gates.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
