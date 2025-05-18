import time
import sys

def typewriter_effect(text, delay=0.08):
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

def main():
    """
    Main function to interact with the user through a command-line interface.

    This function continuously prompts the user to send a message to ChatGPT.
    It provides predefined responses based on the user's input:
    
    - If the user inputs 'hola', it responds with a greeting and asks a follow-up question.
    - If the follow-up question is 'cual es la capital de mexico', it provides information about Mexico City.
    - If the user then inputs 'gracias', it responds with a polite acknowledgment.
    - For any other input, it responds with a default message about quesadillas.

    The responses are displayed using a typewriter effect.

    Note:
        The function runs indefinitely until manually terminated.
    """
    while True:
        user_input = input("Enviar mensaje a ChatGPT: ")
        if user_input.lower() == 'hola':
            response = "¡Hola! ¿Cómo estás? ¿En qué te puedo ayudar hoy?"
            typewriter_effect(response)
            follow_up = input("Enviar mensaje a ChatGPT: ")
            if follow_up.lower() == 'cual es la capital de mexico':
                capital_response = ("La capital de México es la Ciudad de México, también conocida como CDMX. "
                                    "Es una de las ciudades más grandes y pobladas del mundo y también el centro "
                                    "político, económico y cultural del país.")
                typewriter_effect(capital_response)
                thanks_follow_up = input("Enviar mensaje a ChatGPT: ")
                if thanks_follow_up.lower() == 'gracias':
                    thanks_response = ("¡De nada! Si tienes más preguntas, no dudes en preguntar. "
                                       "¡Estoy aquí para ayudarte!")
                    typewriter_effect(thanks_response)
        else:
            typewriter_effect("Si, las quesadillas llevan queso.")
            break


if __name__ == "__main__":
    main()