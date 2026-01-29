FROM python:3.10-alpine⁠

COPY app.py app.py

CMD ["python", "app.py"]