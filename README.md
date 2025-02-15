# AI-Chatbot

# AI Chatbot using Google Gemini API

## Overview
This Python script allows you to interact with the Google Gemini AI API to generate AI-powered responses based on user input. It uses `subprocess` to send API requests via `curl` and processes the JSON response.

## Prerequisites
- Python 3 installed on your system
- A valid API key for the Google Gemini API
- Internet connectivity

## How to Obtain Your API Key
To use this chatbot, you need an API key from Google AI Studio:

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Generate an API key and copy it.
4. Replace `'your gemini key here'` in the script with your API key.

## Installation & Setup
1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Ensure Python is installed by running:
   ```sh
   python --version
   ```
4. Update the `GEMINI_API_KEY` variable in the script with your API key.

## Usage
1. Run the script using:
   ```sh
   python chatbot.py
   ```
2. Start chatting by entering text prompts.
3. Type `exit` or `quit` to terminate the chatbot.

## Code Explanation
- **`generate_response(prompt)`**: Sends the user input to the Gemini API and processes the response.
- **`main()`**: Runs an interactive chatbot session in the terminal.
- **`subprocess.run(command, capture_output=True, text=True)`**: Executes the API request via `curl`.
- **Error Handling**: If the API response does not contain valid data, an error message is returned.

## Troubleshooting
- Ensure your API key is correct and not expired.
- Check your internet connection.
- If the API response contains errors, print the full response for debugging.

## License
This project is open-source and free to use.

