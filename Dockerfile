# ------------------------------
# 📦 Base Image
# ------------------------------
FROM python:3.10.11-slim

# ------------------------------
# 🧰 Environment Setup
# ------------------------------
# Prevents Python from buffering logs and writing pyc files
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory inside container
WORKDIR /app

# ------------------------------
# 🗂️ Copy project files
# ------------------------------
COPY . /app

# ------------------------------
# 🧪 Install dependencies
# ------------------------------
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ------------------------------
# 🚀 Expose Streamlit Port
# ------------------------------
EXPOSE 8501

# ------------------------------
# 🏃 Run Streamlit App
# ------------------------------
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
