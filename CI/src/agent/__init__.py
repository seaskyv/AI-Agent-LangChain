"""Registered tools for the agent."""

from agent.tools.calculator import calculate
from agent.tools.weather import get_weather

ALL_TOOLS = [get_weather, calculate]

__all__ = ["ALL_TOOLS", "calculate", "get_weather"]
