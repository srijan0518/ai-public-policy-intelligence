# AI Public Policy Intelligence Platform

An AI-powered public-policy intelligence platform for extracting, classifying, scoring, comparing, and explaining policy documents through an interactive dashboard.

## Core capabilities
- Policy document ingestion and preprocessing
- Named Entity Recognition (NER)
- Zero-shot policy-topic classification
- Explainable policy importance/risk scoring
- Retrieval-Augmented Generation (RAG) question answering
- Policy comparison and change analysis
- Audience-adaptive explanations
- Interactive intelligence dashboard

## Project structure
```text
src/        Core analysis and intelligence modules
assets/     Dashboard and analysis screenshots
config/     Configuration templates
data/       Local sample-data placeholder
models/     Model/cache placeholder
docs/       Synopsis and final report
notebooks/  Experiment notebooks
```

## Setup

Create a virtual environment and install dependencies from `requirements.txt`.

Copy `.env.example` to `.env` and provide your own API/model credentials if required. **Never commit secrets.**

## Status

Academic/project prototype prepared for BSERC project submission. Replace sample connectors and model configuration with the deployment-specific services before production use.
