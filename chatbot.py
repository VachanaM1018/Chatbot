
# AI Chatbot Using Natural Language Processing (NLP)

import nltk
import random
from nltk.stem import PorterStemmer

# Initialize NLP tools
stemmer = PorterStemmer()

# Chatbot responses
intents = {
    "greeting": {
        "words": ["hello", "hi", "hey", "good morning"],
        "responses": [
            "Hello! How can I help you?",
            "Hi! Nice to meet you.",
            "Hey! What can I do for you?"
        ]
    },

    "name": {
        "words": ["name", "called"],
        "responses": [
            "I am an AI chatbot.",
            "You can call me ChatBot!"
        ]
    },

    "help": {
        "words": ["help", "support", "assist"],
        "responses": [
            "Sure! I am here to help you.",
            "Tell me what you need help with."
        ]
    },

    "weather": {
        "words": ["weather", "temperature", "rain"],
        "responses": [
            "I cannot check live weather, but you can use a weather application."
        ]
    },

    "thanks": {
        "words": ["thanks", "thank", "thankyou"],
        "responses": [
            "You're welcome!",
            "Happy to help!"
        ]
    },

    "goodbye": {
        "words": ["bye", "goodbye", "exit"],
        "responses": [
            "Goodbye! Have a nice day!",
            "See you again!"
        ]
    }
}


# Process user input using NLP
def preprocess(text):
    words = nltk.wordpunct_tokenize(text.lower())
    return [stemmer.stem(word) for word in words]


# Generate chatbot response
def chatbot_response(user_input):

    user_words = preprocess(user_input)

    for intent, details in intents.items():

        keywords = [
            stemmer.stem(word)
            for word in details["words"]
        ]

        if any(word in keywords for word in user_words):
            return random.choice(details["responses"])

    return "Sorry, I don't understand. Can you rephrase?"


# Main chatbot program
print("AI Chatbot is running!")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "exit" in user_input.lower():
        break
