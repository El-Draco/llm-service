#!/bin/bash

# Start the Ollama service
ollama serve &

# Wait for the service to start
sleep 2

#Pull embedding model
echo "Pulling embedding model...please wait"
ollama pull mxbai-embed-large
echo "Embedding model ready"

# Pull the mistral model
echo "Pulling mistral model......please wait"
ollama pull mistral
echo "Default mistral model ready"

# Keep the container running
tail -f /dev/null