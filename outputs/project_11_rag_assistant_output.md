# Project 11 Rag Assistant Output

## Command Run

```bash
python answer.py 'What happens if an item is out of stock?'
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
{"answer":"If an item is out of stock...","citations":[{"source":"substitutions.md"}]}
```

## Explanation

RAG answers are grounded in local policy files.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
