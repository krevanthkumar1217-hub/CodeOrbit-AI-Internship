# Task 1: Rule-Based Chatbot
# Author: CodeOrbit Tech Intern
# Description: A simple command-line chatbot that responds using predefined rules,
# keywords, and includes a fallback response for unknown inputs.

def rule_based_chatbot():
    print("Chatbot: Hello! I am your CodeOrbit AI assistant. Type 'bye' to exit.")
    
    while True:
        # Get user input and convert to lowercase for easier keyword matching
        user_input = input("You: ").strip().lower()
        
        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Best of luck with your internship!")
            break
            
        # Rule 1: Greetings
        elif user_input in ["hi", "hello", "hey", "greetings"]:
            print("Chatbot: Hi there! How can I help you with your tasks today?")
            
        # Rule 2: Internship-related query
        elif "internship" in user_input or "codeorbit" in user_input:
            print("Chatbot: This is part of the CodeOrbit Tech Artificial Intelligence Internship!")
            
        # Rule 3: Well-being check
        elif "how are you" in user_input:
            print("Chatbot: I'm running smoothly in Python! How are you doing?")
            
        # Rule 4: Help instructions
        elif "help" in user_input:
            print("Chatbot: You can say hello, ask about the internship, or type 'bye' to exit.")
            
        # Fallback response for unhandled inputs
        else:
            print("Chatbot: I'm sorry, I didn't quite catch that. Try asking something else or type 'help'.")

if __name__ == "__main__":
    rule_based_chatbot()