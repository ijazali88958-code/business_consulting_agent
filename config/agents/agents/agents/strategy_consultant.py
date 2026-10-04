from crewai import Agent

from config.llm import get_llm


def create_strategy_consultant() -> Agent:
    return Agent(
        role="Strategy Consultant",
        goal=(
            "Develop practical business strategies based on the "
            "business analysis and market analysis."
        ),
        backstory=(
            "You are a senior strategy consultant who specializes in "
            "competitive positioning, growth strategies, SWOT analysis, "
            "and strategic decision-making."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
