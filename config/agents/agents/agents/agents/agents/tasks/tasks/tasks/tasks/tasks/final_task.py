from crewai import Task


def create_final_task(
    agent,
    business_input: str,
    business_analysis: Task,
    market_analysis: Task,
    strategy_analysis: Task,
    financial_analysis: Task,
) -> Task:

    return Task(
        description=f"""
You are the Senior Business Consultant.

Prepare a professional consulting report for:

{business_input}

Review all specialist analyses provided by:

- Business Analyst
- Market Researcher
- Strategy Consultant
- Financial Analyst

Produce a single coherent report.

The report must contain:

# Executive Summary

# Business Analysis

# Market Analysis

# Competitive Analysis

# SWOT Analysis

# Business Strategy

# Financial Considerations

# Major Risks

# Recommended Action Plan

# 30-Day Priorities

# 90-Day Priorities

# Final Recommendations

Important rules:

- Do not claim that assumptions are confirmed facts.
- Do not invent statistics.
- Identify missing information.
- Give practical recommendations.
- Keep the final report understandable to a business owner.
""",
        expected_output="""
A professional business consulting report with clear headings,
practical recommendations, assumptions, risks, and an actionable
30-day and 90-day implementation plan.
""",
        agent=agent,
        context=[
            business_analysis,
            market_analysis,
            strategy_analysis,
            financial_analysis,
        ],
    )
