from openai import OpenAI


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


class GPT4Vision:
    def __init__(self):
        """
        Initializes the GPT4Vision class with an OpenAI client.
        """
        self.client = OpenAI()
                
    def create_vision_messages(self, user_prompt, system_prompt, base64_image_list):
        """
        Creates a list of messages formatted for the GPT-4 Vision API.

        Args:
            user_prompt (str): The user prompt to be sent to the API.
            system_prompt (str): The system prompt to be sent to the API.
            base64_image_list (list): A list of base64-encoded images to be included in the messages.

        Returns:
            list: A list of dictionaries representing the formatted messages.
        """
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt
                    }
                ]
            }
        ]
        # Add images
        for base64_image in base64_image_list:
            messages[-1]["content"].append(
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                }
            )

        return messages
    
    def create_text_messages(self, user_prompt, system_prompt):
        """
        Creates a list of messages formatted for the GPT-4 Text API.

        Args:
            user_prompt (str): The user prompt to be sent to the API.
            system_prompt (str): The system prompt to be sent to the API.

        Returns:
            list: A list of dictionaries representing the formatted messages.
        """
        messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        
        return messages
    
    def vision_chat(self, messages, max_tokens=4000):
        """
        Sends messages to the GPT-4 Vision API and returns the response.

        Args:
            messages (list): A list of formatted messages to be sent to the API.
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            str: The content of the response from the API.
        """
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
        
    def text_chat(self, messages, model="gpt-4-1106-preview" ,max_tokens=4000):
        """
        Sends text-only messages to the GPT-4 API and returns the response.

        Args:
            messages (list): A list of formatted text-only messages to be sent to the API.
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            str: The content of the response from the API.
        """
        response = self.client.completions.create(
            model=model,  # or another suitable model
            messages=messages,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content