import re

def extract_keywords(text):
    text = text.lower()
    words = re.findall(r"[a-zA-Z]+", text)

    stopwords = set([
        "the", "and", "or", "to", "in", "for", "with", "a", "an", "of", "on",
        "is", "are", "was", "were", "as", "at", "by", "this", "that", "from",
        "be", "it", "will", "we", "you", "your"
    ])

    keywords = [w for w in words if w not in stopwords and len(w) > 2]

    return list(set(keywords))

def compare_keywords(resume_keywords, jd_keywords):
    matched = sorted(list(set(resume_keywords).intersection(set(jd_keywords))))
    missing = sorted(list(set(jd_keywords) - set(resume_keywords)))

    return matched, missing
