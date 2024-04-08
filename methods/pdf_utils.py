import fitz  # PyMuPDF
import numpy as np
import os
import shutil
import base64
import io


def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns the text from a PDF file.

    Args:
        pdf_path (str): The file path to the PDF from which to extract text.

    Returns:
        str: A string containing the extracted text from the PDF.
    """
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        text = []
        # Iterate over each page
        for page_num, page in enumerate(pdf, start=1):
            # Extract text from the page
            page_text = page.get_text()
            # Add page number and text to the list
            text.append(f"--- Page {page_num} ---\n{page_text}\n")
        # Join all pages text into a single string with page separators
        return "\n".join(text)
    
    
def pdf_to_images(pdf_path):
    """
    Converts a PDF file to images and saves them to a directory.

    Args:
        pdf_path (str): The file path to the PDF to be converted.
    """
    # Extract the PDF name without the ".pdf" extension
    pdf_name = os.path.basename(pdf_path).replace('.pdf', '')
    # Create a directory for the images    
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf_images", pdf_name)
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)
    os.makedirs(images_dir, exist_ok=True)

    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        # Iterate over each page
        for page_num, page in enumerate(pdf, start=1):
            # Get the pixmap of the current page
            pix = page.get_pixmap()
            # Define the image path
            image_path = os.path.join(images_dir, f"page_{page_num}.png")
            # Save the pixmap as an image
            pix.save(image_path)
         
            
def pdf_to_base64_images(pdf_path):
    """
    Converts a PDF file to a list of base64-encoded images.

    Args:
        pdf_path (str): The file path to the PDF to be converted.

    Returns:
        list: A list of strings, each representing a base64-encoded image.
    """
    base64_images = []

    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        # Iterate over each page
        for page_num, page in enumerate(pdf, start=1):
            # Get the pixmap of the current page
            pix = page.get_pixmap()

            # Convert the pixmap to PNG format
            png_data = pix.tobytes(output="png")

            # Create a BytesIO object to store the PNG data
            png_buffer = io.BytesIO(png_data)

            # Encode the PNG data as base64
            base64_image = base64.b64encode(png_buffer.getvalue()).decode("utf-8")

            # Append the base64-encoded image to the list
            base64_images.append(base64_image)

    return base64_images
