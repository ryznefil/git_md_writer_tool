import os
from pathlib import Path

from methods.pdf_to_md import ResearchMDGenerator


"""
DEFINE IN/OUT PATHS
"""
PAPERS_PDF_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers_pdf")
PDF_MDS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs/pdf_mds")
Path(PDF_MDS_FOLDER).mkdir(parents=True, exist_ok=True)


def generate_markdown_from_pdfs(pdf_to_md_generator, papers_pdf_folder, pdf_mds_folder):
    """
    Generates markdown files from a directory of PDFs using a specified markdown generator.

    Args:
        pdf_to_md_generator (ResearchMDGenerator): An instance of ResearchMDGenerator to convert PDFs to markdown.
        papers_pdf_folder (str): The path to the folder containing PDF files to be processed.
        pdf_mds_folder (str): The path to the folder where the generated markdown files will be saved.
    """
    for pdf_file in os.listdir(papers_pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(papers_pdf_folder, pdf_file)                        
            
            try:
                output_file_vision = os.path.join(pdf_mds_folder, f"{os.path.splitext(pdf_file)[0]}_vision_desc.md")
                pdf_to_md_generator.generate_md_from_pdf_vision(pdf_path, output_file_vision)
                print(f"Vision-based markdown generated for {pdf_file}")
            except Exception as e:                
                print(f"Vision-based generation failed for {pdf_file}: {e}")
                try:
                    output_file_text = os.path.join(pdf_mds_folder, f"{os.path.splitext(pdf_file)[0]}_text_desc.md")
                    pdf_to_md_generator.generate_md_from_pdf_text(pdf_path, output_file_text)
                    print(f"Text-based markdown generated for {pdf_file}")
                except Exception as e:
                    print(f"Text-based generation failed for {pdf_file}: {e}")


if __name__ == "__main__":
    pdf_to_md_generator = ResearchMDGenerator()
    generate_markdown_from_pdfs(pdf_to_md_generator, PAPERS_PDF_FOLDER, PDF_MDS_FOLDER)
