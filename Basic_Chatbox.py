import nltk
import random
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!', 'I am doing great, how about you?']),
    (r'what is your name?', ['I am a chatbot created to chat with you!']),
    (r'how old are you?', ['I am ageless, just a bot!']),
    (r'bye|exit|quit', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'what can you do?', ['I can chat with you, answer some basic questions, and have a conversation!']),
    (r'what is your favorite color?', ['I don\'t have preferences, but I think blue is nice!']),
    (r'(.*) your (.*)', ['I am not sure how to respond to that!', 'Let\'s change the topic.']),
    (r'hi|hello', ['Hi!', 'Hello! How can I assist you today?']),
    (r'(.*)', ['I don\'t understand. Can you ask something else?'])
]

# Create the chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def start_chat():
    print("Hi, I am your chatbot. Type 'quit' to end the conversation.")
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Get chatbot response
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
