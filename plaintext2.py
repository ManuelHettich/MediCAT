'''
From PDF to cleaned plaintext. Output ready for LLM paragraph segmentation.
'''

import re
import fitz  # PyMuPDF

def clean_text(text):
    """
    Clean the extracted text by removing unwanted characters and preserving paragraphs.
    """
    # Remove non-ASCII characters and other noise
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Replace multiple newlines with two newlines (preserving paragraphs)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def insert_empty_line_before_pattern(text, pattern):
    """
    Insert an empty line before each occurrence of the specified pattern,
    while keeping the pattern in the text.
    """
    # Define the regex pattern for the specified format (x.x.x)
    regex_pattern = re.compile(pattern)
    # Use the regex pattern to find and replace occurrences with an empty line before the pattern
    modified_text = regex_pattern.sub(r'\n\n\g<0>', text)
    return modified_text

# Load the PDF file and extract text
def process_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = ""

    # Extract text from each page and apply cleaning
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text()
        extracted_text += clean_text(page_text) + "\n\n"

    # Define the pattern (x.x.x)
    pattern = r'\b\d+\.\d+\.\d+\b'
    
    # Modify the text to insert empty lines before the pattern
    modified_text = insert_empty_line_before_pattern(extracted_text, pattern)

    return modified_text

# Example of usage
pdf_path = '2_NG_106_chronic heart failure in adults diagnosis and management.pdf'  # Replace with the path to your PDF file
output_text = process_pdf(pdf_path)

# Save the output text to a file
output_file_path = 'output_text_file2.txt'  # You can change the file name if needed
with open(output_file_path, 'w') as file:
    file.write(output_text)

# Output file path
print(f"Processed text saved to: {output_file_path}")
