from crewai import LLM

from config.settings import GROQ_API_KEY, GROQ_MODEL


def get_llm() -> LLM:
    """Create the shared Groq LLM configuration."""

    return LLM(
        model=f"groq/{GROQ_MODEL}",
        api_key=GROQ_API_KEY,
        temperature=0.2,
        max_tokens=4096,
    )
