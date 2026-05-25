"""Weather lookup tool."""

from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city.

    Args:
        city: Name of the city to look up.

    Returns:
        A string describing the current weather conditions.
    """
    # Replace with a real API call (e.g. OpenWeatherMap, WeatherAPI)
    fake_data: dict[str, str] = {
        "sydney": "22°C, partly cloudy",
        "tokyo": "18°C, rainy",
        "london": "14°C, overcast",
        "new york": "26°C, sunny",
        "san francisco": "16°C, foggy",
    }
    result = fake_data.get(city.lower())
    if result:
        return f"Weather in {city}: {result}"
    return f"Sorry, no weather data available for {city}."
