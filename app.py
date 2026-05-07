import streamlit as st
from agent import run_newsletter_agent

st.title("🗞️ AI Newsletter Agent")

st.caption("Built using LangGraph + Gemini + Tavily Search")

user_goal = st.text_input(
    "What should the newsletter be about?",
    "Latest AI agent news"
)

# Human-in-the-loop toggle
hitl_mode = st.sidebar.toggle("Human-in-the-loop (HITL)")

if st.button("Generate Newsletter"):

    with st.status("Agent is working...", expanded=True) as status:

        st.write("Step 1: Planning & Researching...")

        final_state = run_newsletter_agent.invoke(
            {"goal": user_goal}
        )

        status.update(label="Complete!", state="complete")

    st.subheader("Drafted Newsletter")

    st.markdown(final_state["draft"])

    st.divider()

    st.info(
        f"Agent Self-Reflection:\n\n{final_state['critique']}"
    )

    # Save output
    with open("newsletter_output.md", "w", encoding="utf-8") as f:
        f.write(final_state["draft"])

    st.success(
        "Newsletter saved as newsletter_output.md"
    )