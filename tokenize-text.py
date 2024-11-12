from transformers import BertTokenizer
import sys
import time

# This script tokenizes input text using the BERT tokenizer and prints it with a typewriter effect.

# Functions:
#     typewriter_effect(text, delay=0.1):
#     tokenize_text(text):

# Usage:
#     Run the script and input a message when prompted. The script will tokenize the input text and print the tokens and their corresponding token IDs.


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

def tokenize_text(text):
    """
    Tokenizes the input text using the BERT tokenizer.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        tuple: A tuple containing:
            - tokens (list of str): The list of tokens obtained from the input text.
            - token_ids (list of int): The list of token IDs corresponding to the tokens.
    """
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    return tokens, token_ids


if __name__ == "__main__":
    user_input = input("Enviar mensaje a ChatGPT: ")
    tokens, token_ids = tokenize_text(user_input)
    print("Size:", len(tokens))
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)