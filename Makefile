.PHONY: setup run-backend run-frontend run-mcp run-agents seed test test-contract test-agents demo docker-up docker-down generate-outputs

setup:
	cd backend && python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
	cd frontend && npm install

run-backend:
	cd backend && uvicorn app.main:app --reload --port 8000

run-frontend:
	cd frontend && npm run dev -- --host 0.0.0.0

run-mcp:
	cd mcp-server && python server.py

run-agents:
	cd agents && python graph.py

seed:
	cd backend && python -m app.seed.seed_data

test:
	pytest backend/tests testing

test-contract:
	pytest backend/tests/test_contracts.py testing/contract_tests

test-agents:
	pytest testing/agent_eval_tests testing/prompt_injection_tests

demo:
	cd agents && python graph.py
	cd ucp-flow && python sample_ucp_flow.py
	cd ap2-payment-safety && python simulate_payment_flow.py

docker-up:
	docker compose up --build

docker-down:
	docker compose down

generate-outputs:
	python scripts/generate_outputs.py
