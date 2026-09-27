def get_bot_response(user_input):
    """Takes user input, cleans it, and returns a predefined rule-based response."""
    # Convert input to lowercase and strip extra whitespace for reliable matching
    cleaned_input = user_input.lower().strip()
    
    # Predefined rules using if-elif-else statements
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
        
    elif cleaned_input in ["how are you", "how's it going", "how are you doing"]:
        return "I'm doing great, thank you for asking! How are you?"
        
    elif cleaned_input in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot built to help you practice coding!"
        
    elif cleaned_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a fantastic day!"
        
    else:
        return "I'm sorry, I don't quite understand that phrase yet. Could you try saying 'hello' or 'how are you'?"

def run_chatbot():
    print("=== Welcome to the Rule-Based Chatbot 🤖 ===")
    print("Type your message below. Type 'bye' or 'exit' to quit the chat.\n")
    
    # Loop to keep the conversation going until the user says goodbye
    while True:
        # Input from the user
        user_message = input("You: ")
        
        # Get the response using the helper function
        bot_reply = get_bot_response(user_message)
        
        # Output the response
        print(f"Bot: {bot_reply}\n")
        
        # Break the loop if the user wants to leave
        if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    run_chatbot()
