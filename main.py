import subprocess
import json

# Initialize the Gemini API key
GEMINI_API_KEY = 'AIzaSyBwIJyHSM0NZPyWRAMVt4I-xUl-axmXr1g'

def generate_response(prompt):
    command = [
        "curl",
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + GEMINI_API_KEY,
        "-H", "Content-Type: application/json",
        "-X", "POST",
        "-d", json.dumps({
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        })
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    response = json.loads(result.stdout)
    
    # Debugging: Print the full response
    print("API Response:", response)
    
    if 'candidates' in response and response['candidates']:
        return response['candidates'][0]['content']['parts'][0]['text']
    else:
        return "Sorry, I couldn't generate a response."

def main():
    print("Welcome to the AI Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
