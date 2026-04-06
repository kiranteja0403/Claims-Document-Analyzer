def generate_summary(text: str) -> str:
    clean_text = " ".join(text.split())
    if not clean_text:
        return "No content available for summary."

    sentences = clean_text.split(". ")
    summary_sentences = sentences[:5]
    summary = ". ".join(summary_sentences).strip()

    if summary and not summary.endswith("."):
        summary += "."

    return summary or "Summary could not be generated."