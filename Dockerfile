FROM python:3.10.19-trixie⁠

WORKDIR app

COPY . .

CMD ["python", "app.py"]