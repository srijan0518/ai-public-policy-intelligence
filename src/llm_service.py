import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        from langchain_groq import ChatGroq
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY is missing in .env")
        return ChatGroq(
            api_key=key,
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            temperature=0.15,
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("OPENAI_API_KEY is missing in .env")
        return ChatOpenAI(
            api_key=key,
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0.15,
        )

    raise ValueError("LLM_PROVIDER must be groq or openai")

def generate_policy_explanation(text, audience):
    llm = get_llm()
    prompt = f"""
You are an evidence-grounded public policy information assistant.

Audience: {audience}

Using ONLY the supplied policy text, produce a useful explanation with:
- What the policy is
- What changed or is introduced
- Who is explicitly affected
- Important dates/requirements
- What the audience should understand

Rules:
- Do not invent facts.
- Do not make legal claims.
- If something is absent, say it is not specified.
- Clearly distinguish stated facts from interpretation.
- Use concise headings and bullets.

SOURCE:
{text}
"""
    return llm.invoke(prompt).content

def generate_comparison(a, b):
    llm = get_llm()
    prompt = f"""
Compare POLICY A and POLICY B strictly using the supplied text.

Return:
## Common Provisions
## New / Added Provisions
## Removed Provisions
## Changed Requirements
## Changed Dates / Financial Provisions
## Explicitly Mentioned Affected Stakeholders
## Uncertain / Not Determinable

Do not invent differences.

POLICY A:
{a}

POLICY B:
{b}
"""
    return llm.invoke(prompt).content
