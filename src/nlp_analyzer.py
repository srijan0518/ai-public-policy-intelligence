import os
import re
from functools import lru_cache

CATEGORIES = [
    "Education",
    "Healthcare",
    "Agriculture",
    "Technology",
    "Cybersecurity",
    "Energy",
    "Environment",
    "Finance",
    "Transport",
    "Industry",
    "Employment",
    "Defence",
    "General Policy",
]

@lru_cache(maxsize=1)
def get_nlp():
    import spacy
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        return None

def extract_entities(text):
    nlp = get_nlp()
    entities = {
        "people": [],
        "organizations": [],
        "locations": [],
        "dates": [],
        "money": [],
    }

    if nlp:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["people"].append(ent.text)
            elif ent.label_ == "ORG":
                entities["organizations"].append(ent.text)
            elif ent.label_ in ("GPE", "LOC"):
                entities["locations"].append(ent.text)
            elif ent.label_ in ("DATE", "TIME"):
                entities["dates"].append(ent.text)
            elif ent.label_ == "MONEY":
                entities["money"].append(ent.text)

    entities["dates"] += re.findall(
        r"\b(?:19|20)\d{2}\b|\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        text,
    )
    entities["money"] += re.findall(
        r"(?:₹|Rs\.?|INR|\$|USD)\s?[\d,]+(?:\.\d+)?",
        text,
        flags=re.I,
    )

    return {
        k: list(dict.fromkeys(v))[:30]
        for k, v in entities.items()
    }

def keyword_category(text):
    lower = text.lower()
    terms = {
        "Education": ["education", "school", "university", "student", "scholarship"],
        "Healthcare": ["health", "hospital", "medical", "healthcare", "patient"],
        "Agriculture": ["agriculture", "farmer", "crop", "irrigation"],
        "Technology": ["technology", "digital", "artificial intelligence", "software"],
        "Cybersecurity": ["cybersecurity", "cyber attack", "ransomware", "malware"],
        "Energy": ["energy", "solar", "renewable", "electricity", "ev"],
        "Environment": ["environment", "climate", "emission", "pollution"],
        "Finance": ["finance", "tax", "bank", "budget", "investment"],
        "Transport": ["transport", "railway", "road", "aviation", "vehicle"],
        "Industry": ["industry", "manufacturing", "msme", "factory"],
        "Employment": ["employment", "worker", "labour", "workforce", "job"],
        "Defence": ["defence", "military", "armed forces"],
    }

    scores = {
        category: sum(lower.count(term) for term in terms)
        for category, terms in terms.items()
    }
    best = max(scores, key=scores.get)
    return best if scores[best] else "General Policy"

def zero_shot_category(text):
    try:
        from transformers import pipeline
        classifier = pipeline(
            "zero-shot-classification",
            model=os.getenv(
                "ZERO_SHOT_MODEL",
                "valhalla/distilbart-mnli-12-3",
            ),
        )
        result = classifier(
            text[:5000],
            CATEGORIES,
            multi_label=False,
        )
        return result["labels"][0], float(result["scores"][0])
    except Exception:
        return keyword_category(text), 0.50

def analyze_document(text):
    entities = extract_entities(text)
    category, category_score = zero_shot_category(text)

    words = len(text.split())
    confidence = (
        "High" if words >= 350 and category_score >= 0.65
        else "Medium" if words >= 120
        else "Low"
    )

    summary = " ".join(text.split())[:900]
    if len(text) > 900:
        summary += "..."

    return {
        "category": category,
        "category_score": category_score,
        "confidence": confidence,
        "entities": entities,
        "summary": summary,
        "word_count": words,
    }
