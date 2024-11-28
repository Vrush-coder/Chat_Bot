import nltk  
import spacy  
from nltk.chat.util import Chat, reflections  

# Load SpaCy language model  
nlp = spacy.load('en_core_web_sm')  
# Define patterns and responses  
pairs = [  
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),  
    (r"what is your name?", ["I'm a chatbot created by [Your Name]."]),  
    (r"how are you?", ["I'm just a program, but I'm here to help you!"]),  
    (r"bye|exit", ["Goodbye! Have a great day!"]),  
    (r"(.*)", ["I'm sorry, I don't understand that. Can you rephrase?"])  
]  

# Initialize Chat  
chatbot = Chat(pairs, reflections)  
print("Chatbot: Hello! How can I assist you today?")  
chatbot.converse()  
# Analyze user input  
def process_input(user_input):  
    doc = nlp(user_input)  
    for ent in doc.ents:  
        print(f"Detected entity: {ent.text} ({ent.label_})")  

while True:  
    user_input = input("You: ")  
    if user_input.lower() in ['bye', 'exit']:  
        print("Chatbot: Goodbye!")  
        break  
    process_input(user_input)  
    print("Chatbot: I'm processing your query!")  

