FROM ollama/ollama:rocm

# Copy any necessary scripts or configuration files
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Entry point
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]