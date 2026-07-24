class PromptBuilder:

    @staticmethod
    def build(context: str, question: str) -> str:

        return f"""
You are an Enterprise AI Knowledge Assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, say:

"I couldn't find that information in the uploaded documents."

--------------------
Context:
{context}
--------------------

Question:
{question}

Answer:
"""