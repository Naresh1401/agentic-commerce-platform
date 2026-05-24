# Project 06 Multi Agent Output

## Command Run

```bash
cd agents && python graph.py
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
{"intent":"meal_planning_cart_checkout","requires_confirmation":true,"final_response":"Cart is prepared."}
```

## Explanation

Supervisor and sub-agents coordinate through shared state.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
