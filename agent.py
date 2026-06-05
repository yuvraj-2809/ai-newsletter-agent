import os
from typing import TypedDict, List

from dotenv import load_dotenv

from langgraph.graph import StateGraph, END

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.tools.tavily_search import TavilySearchResults



# LOAD ENV VARIABLES


load_dotenv()



# LLM SETUP


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)



# SEARCH TOOL


search_tool = TavilySearchResults(k=3)



# STATE


class AgentState(TypedDict):

    goal: str
    queries: List[str]
    content: List[str]
    draft: str
    critique: str



# NODE 1 — PLANNER


def planner(state: AgentState):

    prompt = f"""
    Generate 3 search queries to research this topic:

    {state['goal']}
    """

    response = llm.invoke(prompt)

    queries = response.content.split("\n")

    return {"queries": queries}



# NODE 2 — RESEARCHER


def researcher(state: AgentState):

    all_news = ""

    for query in state["queries"]:

        search_results = search_tool.invoke(query)

        all_news += str(search_results)
        all_news += "\n\n"

    return {"content": [all_news]}



# NODE 3 — WRITER


def writer(state: AgentState):

    prompt = f"""
    Create a professional Markdown newsletter
    using this research:

    {state['content']}

    Include:
    - Title
    - Intro
    - Top stories
    - Conclusion
    """

    response = llm.invoke(prompt)

    return {"draft": response.content}



# NODE 4 — REFLECTOR


def reflector(state: AgentState):

    prompt = f"""
    Critique this newsletter.

    Check:
    - clarity
    - structure
    - engagement
    - professionalism

    Suggest improvements.

    Newsletter:
    {state['draft']}
    """

    response = llm.invoke(prompt)

    return {"critique": response.content}



# GRAPH CONSTRUCTION


builder = StateGraph(AgentState)

builder.add_node("planner", planner)

builder.add_node("researcher", researcher)

builder.add_node("writer", writer)

builder.add_node("reflector", reflector)


builder.set_entry_point("planner")

builder.add_edge("planner", "researcher")

builder.add_edge("researcher", "writer")

builder.add_edge("writer", "reflector")

builder.add_edge("reflector", END)



# COMPILE GRAPH


run_newsletter_agent = builder.compile()
