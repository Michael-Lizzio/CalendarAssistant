"""
Author: Michael Lizzio
Date: 9/9/2024
File: chatgpt.py
"""

# imports
from openai import OpenAI
from old.secret import CHAT_GPT_API


# Main ChatGPT class for ai functions
class ChatGPT:
    def __init__(self, api_key=CHAT_GPT_API):
        # Initialize the OpenAI client with API key
        self.client = OpenAI(api_key=api_key)

    # main function used for prompting gpt
    def prompt_gpt(self, context, text):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": context},
                {"role": "user", "content": text}
            ]
        )

        # Return the raw unfiltered content form chatgpt
        raw_content = response.choices[0].message.content
        return raw_content


# Main function
def main():
    a = ChatGPT()


# Call the main function
if __name__ == "__main__":
    main()
