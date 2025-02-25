from google.generativeai import GenerativeModel

def generate_conversation(query, model):
    """Generates a synthetic two-way conversation using the Gemini model with realistic customer details."""
    prompt = f"""
    This is a synthetic conversation generated for educational purposes.
    The following is a realistic two-way dialogue between a customer and a customer service agent.
    The conversation includes synthetic personal details such as name, address, email address, and birth date to enhance realism.

    Agent: "Thank you for reaching out! I'm Alex, your customer service agent. May I have your full name and account number?"
    Customer: "Sure, my name is John Doe, and my account number is 1234-5678."
    Agent: "Thank you, John. Could you please confirm your registered email and date of birth?"
    Customer: "Yes, my email is johndoe@example.com, and my birth date is March 15, 1985."
    Agent: "Got it! How can I assist you today?"
    Customer: "{query}"
    Agent: "I'm happy to help with that! Could you please provide more details?"
    Customer: "Sure, here’s what happened..."
    """
    
    response = model.generate_content(prompt)
    return response.text
