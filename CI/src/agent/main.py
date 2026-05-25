"""CLI entry point — run the agent interactively."""

from __future__ import annotations

import sys

from dotenv import load_dotenv

from agent.agent import build_agent


def main() -> None:
    """Start an interactive REPL for the agent."""
    load_dotenv()

    print("🤖 LangChain Agent")
    print("   Type your question, or 'quit' to exit.\n")

    executor = build_agent()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            sys.exit(0)

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit", "q"}:
            print("Bye!")
            break

        try:
            result = executor.invoke({"input": user_input})
            print(f"\nAgent: {result['output']}\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()
