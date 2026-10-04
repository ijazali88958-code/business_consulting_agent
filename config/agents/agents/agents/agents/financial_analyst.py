from crewai import Agent

from config.llm import get_llm


def create_financial_analyst() -> Agent:
    return Agent(
        role="Financial Analyst",
        goal=(
            "Evaluate the business's revenue model, pricing, costs, "
            "financial risks, and basic financial feasibility."
        ),
        backstory=(
            "You are a business financial analyst who converts business "
            "strategies into understandable financial considerations."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
