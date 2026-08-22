# AI-POWERED PUBLIC POLICY INTELLIGENCE AND ANALYSIS SYSTEM

## An End-to-End NLP, Retrieval-Augmented Generation & Policy Intelligence Platform

> **Submission note:** The submission-ready DOCX/PDF report contains the formatted figures and dashboard screenshots. This Markdown version provides the GitHub-readable textual report. Dashboard numbers shown in the showcase are illustrative demonstration values unless separately validated by an experimental dataset.

## 1. Introduction

### 1.1 Background & Motivation

Government policies, notifications, regulations, schemes, circulars and public announcements are distributed across many documents and information sources. The increasing volume and unstructured nature of this information make manual review time-consuming and make it difficult for citizens, researchers, businesses and public-sector personnel to identify important changes quickly. The proposed system applies NLP, Generative AI and RAG to transform policy documents into structured, searchable and understandable policy intelligence.

### 1.2 Problem Statement & Public Policy Intelligence Domain

The central challenge is converting unstructured policy information into reliable intelligence about what a policy contains, what has changed, which entities and sectors are explicitly mentioned, and how the information can be explained to different audiences.

## 2. Requirements and Design Objectives

### 2.1 Functional Requirements

- Document ingestion
- Text extraction and chunking
- Named Entity Recognition
- Zero-shot policy classification
- Explainable importance scoring
- Semantic retrieval
- Grounded question answering
- Policy version comparison
- Audience adaptation
- Interactive dashboard

### 2.2 Non-Functional & Architectural Objectives

- Explainability
- Grounding and source traceability
- Modularity
- Usability
- Scalability
- Maintainability

## 3. About Data Collected

### 3.1 Policy Document Sources

The initial system is designed around controlled policy documents supplied by the user. Suitable sources include government notifications, policy documents, circulars, public reports, schemes and selected official press releases. The current implementation does not claim comprehensive real-time coverage.

### 3.2 Document Extraction & Preprocessing

PDFs are processed using PyPDF. Extracted text is normalized and divided into overlapping chunks. Each chunk retains source filename and chunk number for retrieval traceability.

### 3.3 Dataset Schema & Attributes

- source
- chunk
- text
- category
- category_score
- entities
- importance_score
- importance_level

## 4. Tools Used

Python; Streamlit; LangChain; spaCy; Hugging Face Transformers; Sentence Transformers; FAISS; PyPDF; Groq/Llama or OpenAI-compatible LLM; Git & GitHub.

## 5.1 End-to-End System Dataflow Architecture

The system follows a modular dataflow architecture consistent with the project's implementation:

**Figure 5.1 — End-to-End Public Policy Intelligence Dataflow**

1. Policy document input
2. PDF/text extraction
3. Cleaning and chunking
4. NLP / NER extraction
5. Zero-shot policy-domain classification
6. Explainable importance scoring
7. Embedding and FAISS indexing
8. Semantic retrieval
9. Grounded LLM response generation
10. Dashboard presentation, comparison and audience-adaptive views

## 6. Policy Intelligence & Analysis Engine

### 6.1 Importance Scoring Model

The score combines observable document signals such as policy-domain identification, organization references, geographic references, dates, financial references, source length and classification confidence. It is intended to prioritize documents for human review.

### 6.2 Evidence-Grounded Q&A

The policy assistant performs semantic retrieval before generation and presents source/chunk references so users can inspect the evidence.

### 6.3 Policy Version Comparison

The comparison engine identifies common, added, removed and changed provisions and explicitly reports uncertainty where a difference cannot be established.

# 7. Results, Experimental Evaluation & Key Metrics

The original threat-intelligence report evaluates its pipeline on a defined benchmark dataset and reports concrete distributions for NER, zero-shot event classification and severity levels. For the Public Policy Intelligence project, the implementation currently defines the evaluation methodology and dashboard outputs, but no verified benchmark dataset or measured accuracy values have been supplied yet. Therefore, this section distinguishes between metrics that must be measured experimentally and dashboard outputs already defined by the implementation. This avoids presenting invented accuracy numbers as project results.

## 7.1 Evaluation Dataset and Experimental Protocol

A controlled evaluation set should contain representative policy documents from the selected project domain. Each document should be manually annotated for policy category and important entities. For RAG evaluation, a question set should be created with source-backed answers. For policy comparison, pairs of earlier/newer policy versions should be annotated with known changes. A fixed evaluation split should be kept separate from documents used during development.

## 7.2 NLP Evaluation Metrics

Policy classification is evaluated using accuracy and macro-F1 because policy categories may be imbalanced. NER is evaluated using entity-level precision, recall and F1. These metrics should be computed against manually annotated test samples.

## 7.3 RAG Evaluation Metrics

The RAG pipeline should be evaluated separately for retrieval and generation. A response should not be considered successful merely because it is fluent; the claims must be supported by retrieved policy evidence.

## 7.4 Policy Comparison Evaluation

For policy-version comparison, each annotated pair should contain a reference list of added, removed and changed provisions. The system output can then be compared with the reference annotations.

## 7.5 Explainable Importance Score Evaluation

The importance score is an analytical prioritization mechanism rather than a prediction of policy success or economic impact. Evaluation should therefore measure agreement with human reviewers. Reviewers can assign Low, Medium, High or Critical priority to documents and compare those labels with the system's score bands.

## 7.6 Dashboard Performance and Usability Metrics

- Document processing time
- Question response time
- Comparison response time
- Task completion rate
- Source traceability success
- Usability rating

## 7.7 Evaluation Status

| Area | Current Status | What Must Be Added for Final Results |
|---|---|---|
| Document ingestion | Implemented in prototype | Test across representative PDFs |
| NLP / NER | Implemented | Create annotated test set and calculate P/R/F1 |
| Zero-shot classification | Implemented | Create labeled test set and calculate accuracy/macro-F1 |
| Importance scoring | Implemented | Human review and agreement study |
| FAISS retrieval | Implemented | Question/evidence benchmark and retrieval metrics |
| RAG generation | Implemented | Groundedness/completeness evaluation |
| Policy comparison | Implemented | Annotated policy-pair benchmark |
| Dashboard | Implemented as Streamlit UI | Measure task completion, response time and usability |

### Core NLP metrics

| Metric | Formula / Definition | Purpose |
|---|---|---|
| Accuracy | Correct predictions / Total predictions | Overall classification correctness |
| Precision | TP / (TP + FP) | Measures false-positive control |
| Recall | TP / (TP + FN) | Measures missed relevant items |
| F1-score | 2 × Precision × Recall / (Precision + Recall) | Balances precision and recall |
| Macro-F1 | Mean F1 across classes | Fair treatment of minority policy domains |

### RAG metrics

| Metric | What is measured | Target interpretation |
|---|---|---|
| Retrieval Relevance@K | How many retrieved chunks are relevant | Higher means better evidence retrieval |
| Context Precision | Relevant retrieved passages relative to retrieved passages | Lower irrelevant context |
| Groundedness | Answer claims supported by retrieved evidence | Higher factual traceability |
| Answer Completeness | Question requirements addressed by the answer | Higher task coverage |
| Unsupported Claim Rate | Claims not supported by retrieved evidence | Lower is better |
| Citation / Source Traceability | Answers linked to source and chunk | Higher auditability |

### Policy comparison metrics

- Change Precision
- Change Recall
- Change F1
- Unsupported Change Rate
- Comparison Completeness

### Importance-score metrics

- Human Agreement
- Score-Band Agreement
- Rank Correlation
- Reason Validity

# 9. Interactive Dashboard Feature Showcase

The following figures are representative dashboard mockups generated from the implemented V2 interface structure. They are included to show how the report's dashboard section should look; the numerical values shown in the mockups are illustrative and are not claimed experimental results.

### Figure 9.1 — Actual Rendered Policy Intelligence Dashboard Screenshot

The dashboard presents indexed-chunk KPIs, high-importance counts, average importance, policy-domain distribution, recent policy intelligence, entity indicators and system-module status in an application-style layout.

### Figure 9.2 — Policy Analysis and Explainable Importance Score

This view presents extracted entities, policy domain, confidence, importance score and the visible reasons contributing to the score.

### Figure 9.3 — Policy Version Comparison

This view compares earlier and newer policy texts and reports common, added, removed, changed and uncertain provisions.

### Figure 9.4 — RAG-Based Policy Assistant with Evidence

This view provides a grounded answer and lists the source/chunk evidence used by the retrieval pipeline.

### Figure 9.5 — Audience-Adaptive Policy Explanation

This view adapts the explanation for Citizen, Industry, Government Officer or Student audiences.

### 9.6 Dashboard Feature Mapping

| Dashboard Tab | Primary Features | Key Outputs |
|---|---|---|
| Policy Intelligence Dashboard | KPIs, category distribution, intelligence feed | Counts, importance levels, domain analytics |
| Policy Analysis | NER, classification, score explanation | Entities, domain, confidence, importance reasons |
| Policy Comparison | Earlier vs newer policy | Added, removed, changed and uncertain provisions |
| RAG Policy Assistant | Semantic retrieval + LLM | Grounded answer + source/chunk evidence |
| Audience View | Citizen/Industry/Government/Student | Audience-specific explanation |

# 8. Future Enhancements & Conclusion

## 8.1 Future Enhancements

- Official government APIs/RSS feeds
- Persistent cloud vector store
- Automatic policy change alerts
- Multilingual policy analysis
- Geospatial policy visualization
- Historical sector datasets
- Advanced RAG evaluation
- Authentication and role-based access

## 8.2 Project Conclusion

The project demonstrates the integration of NLP, Generative AI, RAG and explainable analytics into a unified public-policy information platform. It transforms unstructured policy documents into searchable intelligence, supports policy comparison and evidence-grounded question answering, and adapts explanations to different audiences. The system remains an academic information-analysis and decision-support prototype and does not replace official policy interpretation.

## References

- Python Documentation
- Streamlit Documentation
- LangChain Documentation
- spaCy Documentation
- Hugging Face Transformers Documentation
- FAISS Documentation
- Sentence Transformers Documentation
- PyPDF Documentation
