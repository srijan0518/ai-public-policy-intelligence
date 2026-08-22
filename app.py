import streamlit as st
from src.document_processor import load_documents
from src.nlp_analyzer import analyze_document
from src.importance_scorer import calculate_importance
from src.rag_engine import build_vectorstore, answer_question
from src.policy_comparator import compare_policies

st.set_page_config(page_title="Policy Intelligence V2", page_icon="🏛️", layout="wide")

st.title("🏛️ AI-Powered Public Policy Intelligence & Analysis System")
st.caption("NLP • Zero-Shot Classification • RAG • Explainable Scoring • Audience-Adaptive Analysis")

if "docs" not in st.session_state:
    st.session_state.docs = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "analyses" not in st.session_state:
    st.session_state.analyses = []

with st.sidebar:
    st.header("1. Upload Sources")
    files = st.file_uploader(
        "Policy PDFs / TXT / Markdown",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
    )

    if st.button("🚀 Process & Index", use_container_width=True):
        if not files:
            st.warning("Upload at least one policy document.")
        else:
            with st.spinner("Extracting, chunking and indexing documents..."):
                docs = load_documents(files)
                st.session_state.docs = docs
                st.session_state.analyses = [
                    analyze_document(d.page_content) for d in docs
                ]
                st.session_state.vectorstore = build_vectorstore(docs)
            st.success(f"Indexed {len(docs)} document chunks.")

    st.divider()
    st.caption("Use official source documents for factual verification.")

tabs = st.tabs([
    "📊 Dashboard",
    "🔍 Policy Intelligence",
    "⚖️ Compare",
    "💬 Ask Policy",
    "👥 Audience View",
])

with tabs[0]:
    st.subheader("Policy Intelligence Dashboard")

    if not st.session_state.docs:
        st.info("Upload policy documents and click Process & Index.")
    else:
        analyses = st.session_state.analyses
        scores = [calculate_importance(a) for a in analyses]

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Document Chunks", len(analyses))
        c2.metric("High Importance", sum(x["score"] >= 70 for x in scores))
        c3.metric("Average Importance", round(sum(x["score"] for x in scores) / len(scores)))
        c4.metric("Domains", len(set(x["category"] for x in analyses)))

        categories = {}
        for a in analyses:
            categories[a["category"]] = categories.get(a["category"], 0) + 1

        st.markdown("### Policy Domain Distribution")
        st.bar_chart(categories)

        st.markdown("### Policy Intelligence Feed")
        for i, (doc, analysis, score) in enumerate(zip(
            st.session_state.docs, analyses, scores
        ), 1):
            with st.expander(
                f"{i}. {doc.metadata.get('source', 'Unknown')} — "
                f"{analysis['category']} — Importance {score['score']}/100"
            ):
                st.write(analysis["summary"])
                st.write("**Entities:**", analysis["entities"])
                st.write("**Scoring reasons:**")
                for reason in score["reasons"]:
                    st.write("•", reason)

with tabs[1]:
    st.subheader("🔍 Policy Intelligence")

    if not st.session_state.docs:
        st.info("Process documents first.")
    else:
        idx = st.selectbox(
            "Select policy chunk",
            range(len(st.session_state.docs)),
            format_func=lambda x: (
                f"{x + 1}. {st.session_state.docs[x].metadata.get('source', 'Unknown')}"
            ),
        )

        analysis = st.session_state.analyses[idx]
        score = calculate_importance(analysis)

        c1, c2, c3 = st.columns(3)
        c1.metric("Domain", analysis["category"])
        c2.metric("Importance", f"{score['score']}/100")
        c3.metric("Confidence", analysis["confidence"])

        st.markdown("### Summary")
        st.write(analysis["summary"])

        st.markdown("### Extracted Information")
        for k, v in analysis["entities"].items():
            st.write(f"**{k.title()}:** {', '.join(v) if v else 'None detected'}")

        st.markdown("### Explainable Importance Score")
        for reason in score["reasons"]:
            st.write("•", reason)

        st.markdown("### Source")
        st.text_area(
            "Policy text",
            st.session_state.docs[idx].page_content,
            height=350,
            label_visibility="collapsed",
        )

with tabs[2]:
    st.subheader("⚖️ Policy Version Comparison")

    if len(st.session_state.docs) < 2:
        st.info("Upload at least two documents/chunks.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            a = st.selectbox(
                "Policy A / Earlier Version",
                range(len(st.session_state.docs)),
                key="compare_a",
            )
        with col2:
            b = st.selectbox(
                "Policy B / Newer Version",
                range(len(st.session_state.docs)),
                key="compare_b",
            )

        if a == b:
            st.warning("Choose two different documents/chunks.")
        elif st.button("Compare", type="primary"):
            with st.spinner("Comparing policy provisions..."):
                result = compare_policies(
                    st.session_state.docs[a].page_content,
                    st.session_state.docs[b].page_content,
                )
            st.markdown(result)

with tabs[3]:
    st.subheader("💬 Ask the Policy Knowledge Base")

    if st.session_state.vectorstore is None:
        st.info("Build the knowledge base first.")
    else:
        question = st.text_input(
            "Question",
            placeholder="What changed and which sectors are explicitly mentioned?",
        )

        if st.button("Ask", type="primary") and question:
            with st.spinner("Retrieving evidence..."):
                answer, sources = answer_question(
                    st.session_state.vectorstore, question
                )

            st.markdown("### Grounded Answer")
            st.write(answer)

            st.markdown("### Evidence Used")
            for source in sources:
                st.write("•", source)

with tabs[4]:
    st.subheader("👥 Audience-Adaptive Explanation")

    if not st.session_state.docs:
        st.info("Process documents first.")
    else:
        idx = st.selectbox(
            "Policy",
            range(len(st.session_state.docs)),
            format_func=lambda x: st.session_state.docs[x].metadata.get("source", "Unknown"),
            key="audience_policy",
        )
        audience = st.selectbox(
            "Explain for",
            ["Citizen", "Industry", "Government Officer", "Student"],
        )

        if st.button("Generate Audience View", type="primary"):
            from src.llm_service import generate_policy_explanation

            with st.spinner("Generating explanation..."):
                result = generate_policy_explanation(
                    st.session_state.docs[idx].page_content,
                    audience,
                )
            st.markdown(result)

st.divider()
st.caption(
    "Academic decision-support prototype. It does not provide legal advice or make governmental decisions."
)
