import streamlit as st

from crew.consulting_crew import build_consulting_crew
from utils.validation import validate_business_input


st.set_page_config(
    page_title="AI Business Consultant",
    page_icon="💼",
    layout="wide",
)


def main():
    st.title("💼 AI Business Consulting Team")

    st.write(
        "A multi-agent business consulting system powered by "
        "CrewAI and Groq."
    )

    st.divider()

    st.subheader("Describe Your Business")

    business_input = st.text_area(
        "Business information",
        placeholder=(
            "Example:\n\n"
            "I want to start an online clothing business targeting "
            "young customers in Pakistan. I want to sell affordable "
            "casual clothing through social media and an online store..."
        ),
        height=250,
    )

    analyze_button = st.button(
        "🚀 Generate Consulting Report",
        type="primary",
        use_container_width=True,
    )

    if analyze_button:

        is_valid, message = validate_business_input(business_input)

        if not is_valid:
            st.warning(message)
            return

        with st.spinner(
            "Our AI consulting team is analyzing your business..."
        ):
            try:
                crew = build_consulting_crew(message)

                result = crew.kickoff()

                st.success("Consulting analysis completed!")

                st.subheader("📊 Consulting Report")

                st.markdown(str(result))

            except Exception as error:
                st.error(
                    "The consulting team could not complete the analysis."
                )

                st.exception(error)


if __name__ == "__main__":
    main()
