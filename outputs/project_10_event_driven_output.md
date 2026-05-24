# Project 10 Event Driven Output

## Command Run

```bash
curl http://localhost:8000/events
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
{"items":[{"event_type":"cart_updated"},{"event_type":"checkout_created"}]}
```

## Explanation

Commerce events are published and replayable.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
