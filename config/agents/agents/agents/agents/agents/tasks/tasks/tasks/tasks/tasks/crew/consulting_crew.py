from crewai import Crew, Process

from agents.business_analyst import create_business_analyst
from agents.market_researcher import create_market_researcher
from agents.strategy_consultant import create_strategy_consultant
from agents.financial_analyst import create_financial_analyst
from agents.senior_consultant import create_senior_consultant

from tasks.business_tasks import create_business_analysis_task
from tasks.market_tasks import create_market_research_task
from tasks.strategy_tasks import create_strategy_task
from tasks.finance_tasks import create_financial_task
from tasks.final_task import create_final_task


def build_consulting_crew(business_input: str) -> Crew:

    business_analyst = create_business_analyst()
    market_researcher = create_market_researcher()
    strategy_consultant = create_strategy_consultant()
    financial_analyst = create_financial_analyst()
    senior_consultant = create_senior_consultant()

    business_task = create_business_analysis_task(
        business_analyst,
        business_input,
    )

    market_task = create_market_research_task(
        market_researcher,
        business_input,
    )

    strategy_task = create_strategy_task(
        strategy_consultant,
        business_input,
        business_task,
        market_task,
    )

    financial_task = create_financial_task(
        financial_analyst,
        business_input,
        business_task,
        strategy_task,
    )

    final_task = create_final_task(
        senior_consultant,
        business_input,
        business_task,
        market_task,
        strategy_task,
        financial_task,
    )

    return Crew(
        agents=[
            business_analyst,
            market_researcher,
            strategy_consultant,
            financial_analyst,
            senior_consultant,
        ],
        tasks=[
            business_task,
            market_task,
            strategy_task,
            financial_task,
            final_task,
        ],
        process=Process.sequential,
        verbose=False,
    )
