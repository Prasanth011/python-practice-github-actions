FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUn pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
