import requests
import time
import sys
from flask import Flask, request, jsonify
import ngrok

# FIRSTLY RUN THE FLASK APP "Run_Flask.ipynb" and then start this to get the response


# Set the auth. token
NGROK_TOKEN = "Put your Ngrok Token Here"
ngrok.set_auth_token(NGROK_TOKEN)

# Start the tunnel
public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")



def suppress_logs():
    """Suppress Werkzeug logs."""
    import os
    import logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

def model_chat():
    """
    Function to continuously chat with a Flask-based model via API.
    Only displays query and response, suppressing Flask server logs.
    """
    suppress_logs()  # Suppress Flask logs if running server locally
    url = "http://127.0.0.1:5000/generate"  # Local URL of the Flask app

    print("Chat with the model! Type 'quit' to end the chat.")

    while True:
        prompt = input("query: ")  # Get user input

        if prompt.lower().strip('"') == "quit":
            print("Exiting the chat. Goodbye!")
            break

        data = {"prompt": prompt.strip('"')}  # Prepare payload

        try:
            start = time.time()  # Corrected variable name
            response = requests.post(url, json=data)
            end = time.time()  # Measure time after receiving response

            if response.status_code == 200:
                print("User : ", data['prompt'])
                print("time taken : ", end-start)
                print(f"KrishiGPT: \"{response.json()['response']}\"")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

# Example Run
if __name__ == "__main__":
    model_chat()
