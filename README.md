# FastAPI Proxy for Ollama

## Overview 
This repository is meant to provide developers with a starting point to move their LLM applications
to production. Simply put, this is a simple fastapi proxy server for Ollama with basic HTTP authentication.
The project comprises two containerized services:
1. `ollama`
2. `fastapi-proxy`

Allows Users to communicate with an LLM using a simple API server that provides basic security.

## Default setup:
- Embedding Model: `mxbai-embed-large`
- LLM: `mistral`

These can be changed easily by modifying the `entrypoint.sh` from the ollama directory.
In this repo, the default models are downloaded from the `entrypoint.sh` script simply for ease of use.
For more LLMs and embeddings model, refer to the official Ollama api on endpoints to pull new models
to the server.

See: https://github.com/ollama/ollama/blob/main/docs/api.md

## Requirements
Any machine with enough memory to support the desired model and Docker installed.

## Instructions
1. Clone & Enter the repository:
```bash
git clone https://github.com/El-Draco/llm-service.git
cd llm-service
```
2. Create a folder `.data` to store all models and ollama data
```bash
mkdir .data
```
3. Follow the `.env.sample` and create a `.env` file with a username and password of your choice
```bash
USERNAME = medhat
PASSWORD = medhat
```
4. Build and run the container
```bash
docker compose up
```
5. Wait for embedding models and llms to download (see logs for status)
6. To test the server open `http://localhost:8000` on your browser or run `curl` from the terminal.
```bash
curl -u USERNAME:PASSWORD http://localhost:8000/
```
You should get the following response: 
```text
Ollama is running
```

## Sample Request:

### Using Python:
```python

# Define the URL of the FastAPI proxy server and the endpoint
url = 'http://localhost:8000/api/chat'

# Define your username and password
username = 'radi'
password = 'radi'

def generate_response(prompt):
    # Define the payload
    payload = {
        'messages': prompt,
        "model": "gemma2:27b-instruct-q6_K",
        # "temperature": "0",
        "stream": False,
    }

    # Make the POST request with HTTP Basic Authentication
    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(username, password)
    )
    return response.json()["message"]["content"]
response = generate_response("Why is the sky blue?")
print('Response:', response)
```

### Sample Request using curl:
```bash
curl -u medhat:medhat http://localhost:8000/api/generate -d '{
  "model": "mistral",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

### To pull a new model

```python
import requests
from requests.auth import HTTPBasicAuth

# Define the URL of the FastAPI proxy server and the endpoint
url = 'http://localhost:8000/api/pull'

# Define your username and password
username = 'your_usernamme'
password = 'your_password'

def pull_model():

    # Define the payload
    payload = {
        "model": "llama3",
    }

    # Make the POST request with HTTP Basic Authentication
    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(username, password)
    )
    print(response.content)
    return response
```