"""Unit tests for agent tools."""

from agent.tools.calculator import calculate
from agent.tools.weather import get_weather


class TestGetWeather:
    def test_known_city(self) -> None:
        result = get_weather.invoke({"city": "Sydney"})
        assert "22°C" in result
        assert "partly cloudy" in result

    def test_known_city_case_insensitive(self) -> None:
        result = get_weather.invoke({"city": "TOKYO"})
        assert "18°C" in result

    def test_unknown_city(self) -> None:
        result = get_weather.invoke({"city": "Atlantis"})
        assert "no weather data" in result.lower()


class TestCalculate:
    def test_basic_arithmetic(self) -> None:
        assert calculate.invoke({"expression": "2 + 3"}) == "5"

    def test_multiplication(self) -> None:
        assert calculate.invoke({"expression": "1500 * 0.85"}) == "1275.0"

    def test_parentheses(self) -> None:
        assert calculate.invoke({"expression": "(10 + 5) * 2"}) == "30"

    def test_division(self) -> None:
        assert calculate.invoke({"expression": "100 / 4"}) == "25.0"

    def test_power(self) -> None:
        assert calculate.invoke({"expression": "2 ** 10"}) == "1024"

    def test_disallowed_characters(self) -> None:
        result = calculate.invoke({"expression": "import os"})
        assert "Error" in result

    def test_division_by_zero(self) -> None:
        result = calculate.invoke({"expression": "1 / 0"})
        assert "Error" in result
