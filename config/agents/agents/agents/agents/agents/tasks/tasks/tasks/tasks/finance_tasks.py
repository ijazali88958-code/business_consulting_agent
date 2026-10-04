from crewai import Task


def create_financial_task(
    agent,
    business_input: str,
    business_analysis: Task,
    strategy_analysis: Task,
) -> Task:

    return Task(
        description=f"""
Evaluate the financial feasibility of this business:

{business_input}

Use the available business and strategy analyses.

Analyze:

1. Revenue model
2. Pricing considerations
3. Main cost categories
4. Potential revenue streams
5. Financial risks
6. Break-even considerations
7. Financial assumptions
8. Recommended financial priorities

Do not invent exact financial figures when the user has not provided them.
Use formulas or ranges when appropriate.
""",
        expected_output="""
A structured financial assessment covering:
- Revenue model
- Pricing
- Costs
- Revenue streams
- Financial risks
- Break-even considerations
- Assumptions
- Recommendations
""",
        agent=agent,
        context=[business_analysis, strategy_analysis],
    )
