from crewai import Task


def create_market_research_task(agent, business_input: str) -> Task:
    return Task(
        description=f"""
Conduct a strategic market analysis for this business:

{business_input}

Analyze:

1. Target market
2. Customer segments
3. Customer needs
4. Competitor categories
5. Competitive advantages
6. Market opportunities
7. Market threats
8. Industry considerations

Do not invent specific market statistics.
Clearly identify assumptions where current data is unavailable.
""",
        expected_output="""
A structured market analysis containing:
- Target market
- Customer segments
- Customer needs
- Competitor analysis
- Opportunities
- Threats
- Competitive positioning
- Important assumptions
""",
        agent=agent,
    )
