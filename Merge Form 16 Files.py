import os
from PyPDF2 import PdfMerger

# Function to merge PDF files based on the first 10 characters of their names
def merge_pdfs_by_prefix(directory):
    pdf_files = {}
    
    # Group PDF files by their first 10 characters
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            prefix = filename[:10]
            if prefix not in pdf_files:
                pdf_files[prefix] = []
            pdf_files[prefix].append(filename)
    
    # Merge PDF files with the same prefix
    for prefix, files in pdf_files.items():
        merger = PdfMerger()
        output_filename = f"{prefix}_Form 16.pdf"
        
        for file in files:
            with open(os.path.join(directory, file), 'rb') as pdf_file:
                merger.append(pdf_file)
        
        with open(os.path.join(directory, output_filename), 'wb') as output_file:
            merger.write(output_file)

# Specify the directory containing the PDF files
directory_path = r"Path/to/Directory"

# Call the function to merge PDF files based on the first 10 characters of their names
merge_pdfs_by_prefix(directory_path)
