"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Agent configuration.

    All values can be overridden via environment variables or a .env file.
    """

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    agent_verbose: bool = True
    agent_max_iterations: int = 10

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
