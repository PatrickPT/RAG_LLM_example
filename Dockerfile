# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#ENV PATH=“${PATH}:/root/.local/bin”

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "rag_chatbot.py"]
