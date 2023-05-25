# Use the official Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .
COPY .env .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory to the container
COPY . .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Set the entrypoint command to run the Streamlit app
CMD ["streamlit", "run", "1_Home.py"]
