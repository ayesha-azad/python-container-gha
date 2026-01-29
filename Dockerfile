FROM python:3.10-alpine⁠

WORKDIR app

COPY . .

CMD ["python", "app.py"]