# Project 05 Single Agent Output

## Command Run

```bash
curl -X POST /agent/single
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
{"intent":"product_search","tools_called":["search_products","get_price","check_inventory"],"requires_confirmation":false}
```

## Explanation

Agent calls tools for deterministic facts.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
