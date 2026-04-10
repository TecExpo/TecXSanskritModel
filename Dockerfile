# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system utilities like bash and curl
RUN apt-get update && apt-get install -y bash curl && rm -rf /var/lib/apt/lists/*

# Install your specific Sanskrit and AI Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your processing logic and automation scripts
COPY sanskrit_processor.py .
COPY process_all.sh .
RUN chmod +x process_all.sh

# Create folders for input and output data
RUN mkdir -p raw_sanskrit tokenized_sanskrit

# Run the batch script by default when the container starts
ENTRYPOINT ["./process_all.sh"]
