FROM python:3.13-slim
WORKDIR /app
COPY index.html calendar.json ./
EXPOSE 8080
CMD ["python3", "-m", "http.server", "8080"]
