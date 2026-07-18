import re


class TextProcessor:

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean extracted PDF text.
        """

        # Remove multiple blank lines
        text = re.sub(r"\n\s*\n", "\n", text)

        # Replace multiple spaces with single space
        text = re.sub(r"[ \t]+", " ", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return text