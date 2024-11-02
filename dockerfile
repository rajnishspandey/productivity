FROM python:3.13.0

# Set the working directory
WORKDIR /usr/src/app/productivity

# Copy only requirements to leverage Docker cache
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Expose the port that your Flask app runs on (default is 5000)
EXPOSE 5000

# Specify the command to run your application
CMD ["python", "main.py"]
