"""Integration tests for the agent (requires OPENAI_API_KEY)."""

import os

import pytest

from agent.agent import build_agent


@pytest.fixture
def executor():
    """Build agent executor; skip if no API key."""
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")
    return build_agent()


class TestAgent:
    def test_weather_query(self, executor) -> None:
        result = executor.invoke({"input": "What's the weather in Sydney?"})
        assert "output" in result
        assert len(result["output"]) > 0

    def test_calculation_query(self, executor) -> None:
        result = executor.invoke({"input": "What is 256 * 4?"})
        assert "1024" in result["output"]

    def test_multi_tool_query(self, executor) -> None:
        result = executor.invoke({
            "input": "What's the weather in Tokyo? Also calculate 99 * 3."
        })
        output = result["output"]
        assert "rainy" in output.lower() or "18" in output
        assert "297" in output
