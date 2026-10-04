from crewai import Task


def create_strategy_task(
    agent,
    business_input: str,
    business_analysis: Task,
    market_analysis: Task,
) -> Task:

    return Task(
        description=f"""
Develop a business strategy for:

{business_input}

Use the Business Analyst's analysis and Market Researcher's analysis.

Develop:

1. Strategic direction
2. SWOT analysis
3. Competitive positioning
4. Customer acquisition strategy
5. Growth strategy
6. Short-term priorities
7. Medium-term priorities
8. Major strategic risks
""",
        expected_output="""
A practical strategic plan containing:
- Strategic direction
- SWOT
- Positioning
- Customer acquisition
- Growth strategy
- Priorities
- Risks
""",
        agent=agent,
        context=[business_analysis, market_analysis],
    )
