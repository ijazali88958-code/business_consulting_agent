def validate_business_input(business_input: str) -> tuple[bool, str]:
    if not business_input:
        return False, "Please describe your business or business problem."

    cleaned = business_input.strip()

    if len(cleaned) < 30:
        return (
            False,
            "Please provide more information about the business. "
            "At least a few sentences will produce better results.",
        )

    if len(cleaned) > 12000:
        return (
            False,
            "Your description is too long. Please keep it below 12,000 characters.",
        )

    return True, cleaned
