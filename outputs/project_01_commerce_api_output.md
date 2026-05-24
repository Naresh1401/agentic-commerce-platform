# Project 01 Commerce Api Output

## Command Run

```bash
curl http://localhost:8000/products?query=milk
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
{"items":[{"sku":"SKU-MILK-001","name":"Organic Whole Milk"}],"count":1}
```

## Explanation

REST product search returns catalog data.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
