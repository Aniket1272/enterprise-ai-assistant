from app.loaders.pdf_loader import PDFLoader


def main():

    text = PDFLoader.load("uploads/sample.pdf")

    print(text)


if __name__ == "__main__":
    main()