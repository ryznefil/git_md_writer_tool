# Project Overview

The project is a Python-based tool designed to generate GitHub repository descriptions from research papers. It leverages OpenAI's GPT-4 models, both text and vision variants, to process PDF documents and create concise, informative markdown summaries suitable for repository documentation. The tool extracts text from PDFs, optionally converts PDF pages to images, and uses these inputs to guide the AI in crafting project descriptions.

# Key Features

- **PDF Text Extraction**: Utilizes PyMuPDF to extract text from research papers.
- **Image Conversion**: Converts PDF pages to base64-encoded images for visual context.
- **AI-Powered Summarization**: Integrates with OpenAI's GPT-4 to generate summaries.
- **Markdown Output**: Saves AI-generated descriptions in markdown format for easy use on GitHub.
- **Error Handling**: Gracefully handles failures by attempting text-only summarization if vision-based summarization fails.

# Installation and Setup

Clone the repository and install the required dependencies, including `fitz` (PyMuPDF) for PDF processing and `openai` for interacting with the GPT-4 API.
```
    git clone <repository-url>
    cd <repository-directory>
    pip install -r requirements.txt
```

# Usage Examples

To generate markdown descriptions from a folder of PDFs:
```
    from methods.pdf_to_md import ResearchMDGenerator
    pdf_to_md_generator = ResearchMDGenerator()
    pdf_to_md_generator.generate_md_from_pdf_vision('path_to_pdf', 'output_md_file')
```

# Contributing

Contributions are welcome! If you have ideas for improvements or want to add features, please open an issue or submit a pull request following the standard GitHub flow.

# License

This project is licensed under the MIT License - see the LICENSE file for details.