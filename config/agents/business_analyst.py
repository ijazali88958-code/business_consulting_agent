from crewai import Agent

from config.llm import get_llm


def create_business_analyst() -> Agent:
    return Agent(
        role="Business Analyst",
        goal=(
            "Analyze the client's business idea, objectives, "
            "customers, business model, and major business challenges."
        ),
        backstory=(
            "You are an experienced business analyst who breaks down "
            "business problems into clear and actionable components."
        ),
        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
    )
