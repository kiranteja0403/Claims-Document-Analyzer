from typing import List

def ask_question(question: str, vectorstore) -> str:
    docs = vectorstore.similarity_search(question, k=4)

    if not docs:
        return "No relevant information found in the document."

    context_parts: List[str] = []
    for doc in docs:
        content = getattr(doc, "page_content", "")
        if content:
            context_parts.append(content.strip())

    context = "\n\n".join(context_parts).strip()

    if not context:
        return "Relevant chunks were retrieved, but no readable content was found."

    return context[:2000]