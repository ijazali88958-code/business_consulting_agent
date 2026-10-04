from crewai import Task


def create_business_analysis_task(agent, business_input: str) -> Task:
    return Task(
        description=f"""
Analyze the following business situation:

{business_input}

Evaluate:

1. Business idea
2. Core problem
3. Target customers
4. Value proposition
5. Business model
6. Business objectives
7. Major challenges
8. Key assumptions

Clearly separate facts from assumptions.
""",
        expected_output="""
A structured business analysis containing:
- Business overview
- Problem definition
- Target customers
- Value proposition
- Business model
- Objectives
- Challenges
- Assumptions
""",
        agent=agent,
    )
