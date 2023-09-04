# Use the official Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the entire app directory to the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501 

# Set Streamlit Healthcheck 
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the entrypoint command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "1_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
