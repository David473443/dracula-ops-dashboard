FROM python:3.13-slim
WORKDIR /app
COPY . .
EXPOSE ${PORT:-8080}
CMD python3 -m http.server ${PORT:-8080}
