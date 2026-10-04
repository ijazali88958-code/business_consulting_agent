from crewai import Agent

from config.llm import get_llm


def create_senior_consultant() -> Agent:
    return Agent(
        role="Senior Business Consultant",
        goal=(
            "Review all consultant analyses and produce one coherent, "
            "professional, practical business consulting report."
        ),
        backstory=(
            "You are a senior management consultant responsible for "
            "combining specialist analyses into executive-level recommendations."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
