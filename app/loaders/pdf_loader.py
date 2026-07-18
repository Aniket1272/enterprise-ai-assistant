from pathlib import Path

from pypdf import PdfReader

from app.processors.text_processor import TextProcessor

class PDFLoader:

    @staticmethod
    def load(file_path: str) -> str:
        """
        Extract all text from a PDF.

        Args:
            file_path: Path to PDF

        Returns:
            Complete extracted text.
        """

        pdf_path = Path(file_path)

        reader = PdfReader(pdf_path)

        extracted_text = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text.append(text)


        raw_text = "\n".join(extracted_text)

        clean_text = TextProcessor.clean(raw_text)        

        return "\n".join(clean_text)