FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /app/server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
