from openai import OpenAI, OpenAIError
from decouple import config
import os
import time
import sys

# This script interacts with the OpenAI ChatGPT model using a typewriter effect for displaying responses.

# Modules:
#     openai: Provides the OpenAI API client and error handling.
#     decouple: Manages environment variables.
#     os: Provides a way to interact with the operating system.
#     time: Provides time-related functions.
#     sys: Provides access to system-specific parameters and functions.

# Functions:
#     typewriter_effect(text, delay=0.1):

#     main():
#         Continuously prompts the user to input a message, sends the message to the ChatGPT model,
#         and prints the response with a typewriter effect. If an error occurs during the API call,
#         it catches the OpenAIError and prints an error message.

# Variables:
#     OPENAI_API_KEY (str): The API key for accessing OpenAI services, retrieved from environment variables.
#     api_key (str): The API key for accessing OpenAI services, retrieved from environment variables.
#     client (OpenAI): The OpenAI API client initialized with the API key.


def typewriter_effect(text, delay=0.1):
    """
    Prints text with a typewriter effect.

    Args:
        text (str): The text to be printed.
        delay (float, optional): The delay between each character. Default is 0.1 seconds.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

OPENAI_API_KEY = config('OPENAI_API_KEY')
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    """
    Main function to interact with ChatGPT.

    This function continuously prompts the user to input a message, sends the message to the ChatGPT model,
    and prints the response with a typewriter effect. If an error occurs during the API call, it catches
    the OpenAIError and prints an error message.

    Raises:
        OpenAIError: If there is an issue with the API call to OpenAI's chat completions.
    """
    while True:
        user_input = input("Enviar mensaje a ChatGPT: ")
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un asistente útil que responde en español."},
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            typewriter_effect(completion.choices[0].message.content)
        except OpenAIError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()