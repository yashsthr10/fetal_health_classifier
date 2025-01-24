FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pandas jinja2 xgboost

EXPOSE 8000

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
