import os
from dotenv import load_dotenv
load_dotenv()

def get_embeddings():
    provider = os.getenv("EMBEDDING_PROVIDER", "huggingface").lower()

    if provider == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(
            model_name=os.getenv(
                "EMBEDDING_MODEL",
                "sentence-transformers/all-MiniLM-L6-v2",
            )
        )

    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(
        model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    )

def build_vectorstore(documents):
    from langchain_community.vectorstores import FAISS
    return FAISS.from_documents(documents, get_embeddings())

def answer_question(vectorstore, question):
    from src.llm_service import get_llm

    docs = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    ).invoke(question)

    context = "\n\n".join(
        f"[{d.metadata.get('source', 'Unknown')} | chunk {d.metadata.get('chunk', '?')}]\n"
        f"{d.page_content}"
        for d in docs
    )

    prompt = f"""
You are a policy intelligence assistant.

Answer ONLY from the evidence below.

Question:
{question}

Evidence:
{context}

Rules:
- Do not invent facts.
- If evidence is insufficient, explicitly say so.
- Cite evidence using [source | chunk].
- Keep facts separate from interpretation.
"""
    answer = get_llm().invoke(prompt).content

    sources = [
        f"{d.metadata.get('source', 'Unknown')} | chunk {d.metadata.get('chunk', '?')}"
        for d in docs
    ]
    return answer, sources
