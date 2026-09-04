FROM python:3.13-slim
WORKDIR /app
COPY index.html calendar.json ./static/
EXPOSE ${PORT:-8080}
CMD python3 -m http.server ${PORT:-8080} --directory static
