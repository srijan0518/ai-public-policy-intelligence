# AI Public Policy Intelligence Platform

An AI-powered public-policy intelligence platform for extracting, classifying, scoring, comparing, and explaining policy documents through an interactive dashboard.

## Core capabilities

- Policy document ingestion and preprocessing
- Named Entity Recognition (NER)
- Zero-shot policy-domain classification
- Explainable policy importance scoring
- Retrieval-Augmented Generation (RAG) question answering
- Policy comparison and change analysis
- Audience-adaptive explanations
- Interactive intelligence dashboard

## Repository structure

```text
ai-public-policy-intelligence/
├── app.py
├── requirements.txt
├── setup.bat
├── .env.example
├── .gitignore
├── src/
│   ├── document_processor.py
│   ├── nlp_analyzer.py
│   ├── importance_scorer.py
│   ├── rag_engine.py
│   ├── llm_service.py
│   └── policy_comparator.py
├── assets/
│   └── dashboard.html
└── docs/
    ├── synopsis/
    │   └── PROJECT_SYNOPSIS.md
    └── report/
        └── PROJECT_REPORT.md
```

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Copy `.env.example` to `.env`, add your own LLM credentials, then run:

```bash
streamlit run app.py
```

## Dashboard showcase

`assets/dashboard.html` contains the rendered dashboard showcase used for the project documentation. The report's Figure 9.1 is the actual rendered dashboard screenshot; Figure 9.2 is retained separately in the report as the policy-analysis/explainable-score view.

## Documentation

- [Project synopsis](docs/synopsis/PROJECT_SYNOPSIS.md)
- [Project report](docs/report/PROJECT_REPORT.md)

## Important note

This is an academic decision-support prototype. It does not provide legal advice, make governmental decisions, or claim that illustrative dashboard values are experimentally validated results. Always verify important policy information against official source documents.

**Never commit `.env`, API keys, passwords, model credentials, or other secrets.**
