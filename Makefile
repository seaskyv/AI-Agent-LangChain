.PHONY: install dev test lint format run clean

# Install production dependencies
install:
	uv sync

# Install with dev dependencies
dev:
	uv sync --extra dev

# Run the agent interactively
run:
	uv run agent

# Run unit tests only (no API key needed)
test:
	uv run pytest tests/test_tools.py -v

# Run all tests including integration (needs OPENAI_API_KEY)
test-all:
	uv run pytest -v --cov=agent

# Lint
lint:
	uv run ruff check src/ tests/
	uv run mypy src/

# Auto-format
format:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

# Clean build artifacts
clean:
	rm -rf dist/ build/ *.egg-info .pytest_cache .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
