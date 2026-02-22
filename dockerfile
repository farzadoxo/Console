FROM python:latest

WORKDIR /console
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3","backend/main.py"]
