import argparse
from bs4 import BeautifulSoup
import os
from pathlib import Path
from pdfminer.high_level import extract_text
from readability import Document
import requests
import textwrap
from transformers import pipeline
from urllib.parse import urlparse

model_path = f"{Path.home()}/LLM/MBZUAI/LaMini-Flan-T5-248M"
summarizer = None

# Read PDF document and extract the text from a range of pages.
def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    return extract_text(pdf_path, page_numbers=range(start_page, end_page+1) if start_page and end_page else None)

# Get the content of a WEB page using the URL.
# @param url: The URL of the WEB page.
def get_url_content(url):
    doc = Document(requests.get(url, stream=True).text)
    return BeautifulSoup(doc.summary(), features="lxml").text

# Check if the input is an existing readable file.
# @param filepath: The path to the file.
# @return: True if the file exists and is readable, False otherwise.
def is_existing_readable_file(filepath: str) -> bool:
    return os.path.isfile(filepath) and os.access(filepath, os.R_OK)

# Check if the input is a well-formatted URL.
# @param s: The input string.
# @return: True if the input is a well-formatted URL, False otherwise.
def is_well_formatted_url(s: str) -> bool:
    try:
        result = urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def main(input_value):
    if is_existing_readable_file(input_value):
        print(f"Summarizing the content of {input_value} ...\n")
        # Get the summary
        summary = summarizer(extract_text_from_pdf(input_value)[0:2200], max_length=350, min_length=25, do_sample=False)
        # Print summary
        print(textwrap.fill(summary[0]['summary_text'], width=80))

    elif is_well_formatted_url(input_value):
        print(f"Summarizing the content of {input_value} ...\n")
        # Get the summary
        summary = summarizer(get_url_content(input_value)[0:2350], max_length=350, min_length=25, do_sample=False)
        # Print summary
        print(textwrap.fill(summary[0]['summary_text'], width=80))

    else:
        print(f"You provided the input: {input_value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple text summarizer CLI.")

    # Add an 'input' argument
    parser.add_argument("input", type=str, help="A file path or a URL.")

    args = parser.parse_args()

    if not os.path.isdir(model_path):
        print(f"The LLM model {model_path} is missing!")
        exit(1)

    print(f"Loading the LLM model from {model_path}...")
    summarizer = pipeline("summarization", model=model_path, tokenizer=model_path)
    print("Done!")

    main(args.input)
