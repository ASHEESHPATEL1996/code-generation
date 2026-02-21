
FROM python:3.13

# Set working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY requirements.txt .

# Install dependencies using uv
RUN uv pip install --system -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]