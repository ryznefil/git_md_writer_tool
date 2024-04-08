from llm_proxy import GPT4Vision
from pdf_utils import (extract_text_from_pdf,
                        pdf_to_base64_images)


SYSTEM_PROMPT_TEMPLATE = """
**ROLE**
You are an AI research assistant tasked with creating concise and informative project descriptions for GitHub repositories based on the user's research papers. 
Your goal is to provide a clear overview of each project, including its purpose, methodology, key findings, and significance. 

**TASK**
You are provided with a text representation of your research paper as well as with a list of images of the PDF file for the research paper.

Your task is to to generate the project descriptions, follow these steps:

1. Carefully read the research paper provided by the user.
2. Identify the main objectives, research questions, or hypotheses of the study.
3. Briefly describe the methods, datasets, or tools used in the project.
4. Summarize the most important results, conclusions, or contributions of the research.
5. Explain the potential impact or applications of the findings.
6. Organize the information into a well-structured, readable format suitable for a GitHub repository description.
7. Aim for a description length of 150-300 words, focusing on the most essential aspects of the project.
8. Use clear, concise language that is accessible to a broad audience, including those who may not be experts in the specific research field.
9. If applicable, mention any collaborators, funding sources, or links to related publications or resources.

**OUTPUT FORMAT**
Please format the project description using markdown syntax, including headers, bullet points, and links where appropriate.

**NOTE**
Remember to maintain a professional and objective tone throughout the project descriptions. 
Your ultimate goal is to provide an engaging and informative summary that encourages others to explore the repository and learn more about the research.
Take your time and think step by step. If you get this right I will give you 100 dollars tip.
"""


USER_PROMPT_TEMPLATE = f"""
PDF Text
{{}}

###

Output markdown formatted text:
"""


class ResearchMDGenerator:
    def __init__(self, api_key):
        """
        Initializes the ResearchMDGenerator class with a GPT4Vision instance.

        Args:
            api_key (str): The API key for the OpenAI client.
        """
        self.gpt4_vision = GPT4Vision(api_key)

    def generate_md_from_pdf(self, pdf_path, output_file):
        """
        Generates a markdown file from a PDF by using the GPT-4 Vision API.

        Args:
            pdf_path (str): The file path to the PDF to be processed.
            output_file (str): The file path where the markdown file will be saved.
        """
        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(pdf_path)

        # Convert PDF to base64 images
        base64_images = pdf_to_base64_images(pdf_path)

        # Create user prompt
        user_prompt = USER_PROMPT_TEMPLATE.format(pdf_text)

        # Create vision messages
        messages = self.gpt4_vision.create_vision_messages(user_prompt, SYSTEM_PROMPT_TEMPLATE, base64_images)

        # Call GPT-4 Vision API
        gpt_response = self.gpt4_vision.vision_chat(messages)

        # Save the response to a markdown file
        with open(output_file, 'w') as f:
            f.write(gpt_response)

        print(f"Generated markdown file: {output_file}")