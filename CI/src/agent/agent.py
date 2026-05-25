"""Build and configure the LangChain agent."""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from agent.config import settings
from agent.tools import ALL_TOOLS

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Use the available tools when you need factual data or calculations. "
    "Always explain your reasoning briefly before giving the final answer."
)


def build_agent() -> AgentExecutor:
    """Create an AgentExecutor wired with all registered tools.

    Returns:
        A ready-to-invoke AgentExecutor instance.
    """
    llm = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    agent = create_tool_calling_agent(llm, ALL_TOOLS, prompt)

    return AgentExecutor(
        agent=agent,
        tools=ALL_TOOLS,
        verbose=settings.agent_verbose,
        max_iterations=settings.agent_max_iterations,
        handle_parsing_errors=True,
    )
