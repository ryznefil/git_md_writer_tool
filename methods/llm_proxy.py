from openai import OpenAI

MODEL_BASE_PARAMS = {              
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "temperature": 0,
            }

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
            **MODEL_BASE_PARAMS
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
        response = self.client.chat.completions.create(
            model=model,  # or another suitable model            
            messages=messages,
            max_tokens=max_tokens,
            **MODEL_BASE_PARAMS
        )
        return response.choices[0].message.content

