# LangChain Agent

A tool-calling AI agent built with LangChain. The agent can reason about user questions, decide which tools to invoke, and synthesize results into a natural language response.

## Features

- **ReAct pattern** — the agent reasons, acts (calls tools), observes results, and repeats until it has a complete answer
- **Extensible tools** — add new tools by dropping a file in `src/agent/tools/`
- **Interactive REPL** — chat with the agent from your terminal
- **CI/CD ready** — GitHub Actions workflow with linting, formatting, and tests

## Quick Start

```bash
# Clone
git clone https://github.com/youruser/langchain-agent.git
cd langchain-agent

# Install (requires uv — https://docs.astral.sh/uv/)
uv sync --extra dev

# Configure
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run
uv run agent
```

## Usage

```
$ uv run agent
🤖 LangChain Agent
   Type your question, or 'quit' to exit.

You: What's the weather in Sydney and what is 1500 * 0.85?

Agent: The weather in Sydney is 22°C and partly cloudy. And 1500 × 0.85 = 1,275.
```

## Project Structure

```
langchain-agent/
├── src/agent/
│   ├── main.py          # CLI entry point (REPL)
│   ├── agent.py          # Agent builder
│   ├── config.py         # Settings from env vars
│   └── tools/
│       ├── __init__.py   # Tool registry
│       ├── weather.py    # Weather lookup
│       └── calculator.py # Math evaluator
├── tests/
│   ├── test_tools.py     # Unit tests (no API key needed)
│   └── test_agent.py     # Integration tests (needs API key)
├── .github/workflows/
│   └── ci.yml            # GitHub Actions
├── pyproject.toml        # Dependencies & project config
├── Makefile              # Convenience commands
└── .env.example          # Environment template
```

## Adding a New Tool

1. Create a file in `src/agent/tools/`, e.g. `search.py`:

```python
from langchain_core.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web for a query."""
    # your implementation
    return results
```

2. Register it in `src/agent/tools/__init__.py`:

```python
from agent.tools.search import web_search

ALL_TOOLS = [get_weather, calculate, web_search]
```

That's it — the agent will automatically discover and use the new tool.

## Development

```bash
make dev          # Install with dev deps
make test         # Unit tests only
make test-all     # All tests (needs OPENAI_API_KEY)
make lint         # Ruff + mypy
make format       # Auto-format
```

## Configuration

| Env Variable           | Default       | Description                  |
|------------------------|---------------|------------------------------|
| `OPENAI_API_KEY`       | (required)    | Your OpenAI API key          |
| `OPENAI_MODEL`         | `gpt-4o-mini` | Model to use                 |
| `AGENT_VERBOSE`        | `true`        | Show reasoning chain         |
| `AGENT_MAX_ITERATIONS` | `10`          | Max tool-call loops          |

## License

MIT
