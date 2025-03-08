FROM python:3.8-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and application code
COPY model/ /app/model/
COPY app/ /app/app/

# Copy the main application file
COPY main.py .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose the port for the FastAPI application
EXPOSE 5000

# Run the FastAPI application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "5000"]