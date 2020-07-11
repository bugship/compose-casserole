FROM python:3.11-alpine
WORKDIR /app
RUN apk add --no-cache wget
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5005
CMD ["python", "app.py"]
