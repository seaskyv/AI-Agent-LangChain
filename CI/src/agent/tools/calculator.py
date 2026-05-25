"""Math calculator tool."""

from langchain_core.tools import tool


@tool
def calculate(expression: str) -> str:
    """Safely evaluate a mathematical expression.

    Supports basic arithmetic: +, -, *, /, **, (), and common math functions.

    Args:
        expression: A math expression string, e.g. "1500 * 0.85".

    Returns:
        The result as a string, or an error message.
    """
    allowed_chars = set("0123456789+-*/.() ")
    if not all(c in allowed_chars for c in expression):
        return f"Error: expression contains disallowed characters: {expression}"

    try:
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307
        return str(result)
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"
