# Project 09 Partner Integration Output

## Command Run

```bash
cd partner-integrations && python retry_and_circuit_breaker_demo.py
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
{"normalized_request":{"sku":"SKU-PASTA-001","store_id":"store_1001","quantity":2}}
```

## Explanation

Partner-specific payloads normalize into internal format.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
