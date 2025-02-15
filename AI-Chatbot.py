from fastapi import FastAPI, Request
import subprocess
import json
import uvicorn

app = FastAPI()

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

@app.post("/generate-response")
async def generate_response_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "Prompt is required"}
    response = generate_response(prompt)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
