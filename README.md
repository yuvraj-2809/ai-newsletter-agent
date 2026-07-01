🚀 **Live Demo:** https://ai-newsletter-agent-d9kusjpde3gbfct7qnsfpz.streamlit.app/

# AI Newsletter Agent

An autonomous AI agent that researches, writes, critiques, and generates newsletters about the latest AI agent news.

---

## Features

- Autonomous multi-step AI workflow
- LangGraph-based agent orchestration
- Gemini LLM integration
- Tavily web search integration
- Self-reflection and critique step
- Human-in-the-loop toggle
- Streamlit frontend UI
- Markdown newsletter generation
- Automated newsletter export

---

## Workflow Architecture

Planner → Researcher → Writer → Reflector

### Agent Steps

1. Plan newsletter research queries
2. Search latest AI agent news using Tavily
3. Generate newsletter draft using Gemini
4. Critique generated newsletter
5. Improve output through reflection
6. Export newsletter as Markdown file

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Gemini API
- Tavily Search API
- Streamlit

---

## Project Structure

```bash
ai-newsletter-agent/
│
├── app.py
├── agent.py
├── README.md
├── requirements.txt
├── .env.example
├── newsletter_output.md
└── screenshots/
