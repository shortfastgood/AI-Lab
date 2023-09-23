# Jupyter Notebooks

## Example N1

Simple summary of a PDF file.

### Additional Libraries

    > pip install pdfminer.six transformers

### Python Code

    from pdfminer.high_level import extract_text
    from transformers import pipeline
    
    # Read PDF document and extract the text from a range of pages.
    def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    return extract_text(pdf_path, page_numbers=range(start_page, end_page+1) if start_page and end_page else None)
    
    # Usage
    pdf_path = '../data/agile-patterns.pdf'
    extracted_text = extract_text_from_pdf(pdf_path, 1, 8)
    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    # Run summarization
    summary = summarizer(extracted_text[0:4000], max_length=200, min_length=100, do_sample=False)
    # Print summary
    print(summary[0]['summary_text'])

## Example N2

Simple summary of a WEB page.

### Addtitional Libraries

    > pip install readability-lxml requests transformers

### Python Code

    from bs4 import BeautifulSoup
    from readability import Document
    import requests
    from transformers import pipeline
    
    # Get the content of a WEB page using the URL.
    def get_content(url):
    doc = Document(requests.get(url, stream=True).text)
    return BeautifulSoup(doc.summary()).text
    
    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    # Run summarization
    summary = summarizer(get_content("https://en.wikipedia.org/wiki/BERT_(language_model)")[0:4000], max_length=200, min_length=100, do_sample=False)
    # Print summary
    print(summary[0]['summary_text'])

