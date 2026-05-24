# Project 13 Guardrails Output

## Command Run

```bash
pytest testing/prompt_injection_tests
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
{"blocked":true,"reason":"prompt_injection"}
```

## Explanation

Negative prompts are detected.

## What The Output Proves

The project module is demonstrable locally and avoids real Kroger APIs, real payments, real customer data, and secrets.
