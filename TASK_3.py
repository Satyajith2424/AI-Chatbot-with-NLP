import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?"]],
    [r"how are you?", ["I'm functioning perfectly. Thanks for asking!"]],
    [r"what is your name\??", ["I'm CODTECH's AI Chatbot."]],
    [r"what can you do\??", ["I can answer basic questions, help you with Python topics, and guide you about this internship."]],
    
    # Internship and project questions
    [r"what is this internship about\??", ["It's a Python Programming internship with tasks like API integration, report generation, and chatbot development."]],
    [r"what is the duration of this internship\??", ["The internship lasts for 4 weeks."]],
    [r"who is offering this internship\??", ["CODTECH IT SOLUTIONS is the provider."]],
    [r"what are the tasks\??", ["Task 1: API & Data Visualization, Task 2: PDF Report Generation, Task 3: AI Chatbot using NLP."]],
    [r"will I get a certificate\??", ["Yes! You’ll receive it on your internship end date."]],
    
    # Python-related questions
    [r"what is python\??", ["Python is a versatile, high-level programming language used for web development, data science, automation, and more."]],
    [r"what is a list in python\??", ["A list is a collection that is ordered and changeable. Example: [1, 2, 3]."]],
    [r"what is a dictionary in python\??", ["A dictionary stores data in key-value pairs. Example: {'name': 'Alice'}."]],
    [r"what is a function in python\??", ["A function is a block of reusable code that performs a specific task."]],
    [r"how to install packages in python\??", ["Use pip, like this: pip install package_name."]],
    [r"what is NLP\??", ["NLP stands for Natural Language Processing. It enables computers to understand human language."]],
    [r"which libraries are used in NLP\??", ["Popular libraries include NLTK, spaCy, and transformers."]],
    [r"bye|exit|quit", ["Goodbye! Best wishes for your internship."]],
    [r"(.*)", ["I'm not sure about that. Try asking something related to Python, internship, or NLP."]]
]
chatbot = Chat(pairs, reflections)
print("🤖 CODTECH AI Chatbot initialized. Type 'bye' to exit.")
chatbot.converse()