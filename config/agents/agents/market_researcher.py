from crewai import Agent

from config.llm import get_llm


def create_market_researcher() -> Agent:
    return Agent(
        role="Market Research Consultant",
        goal=(
            "Analyze the target market, customers, competitors, "
            "industry opportunities, threats, and market positioning."
        ),
        backstory=(
            "You are a strategic market researcher experienced in "
            "customer segmentation, competitive analysis, and market evaluation."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
