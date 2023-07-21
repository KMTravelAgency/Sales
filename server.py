from fastapi import FastAPI
from rabbitmq_helper import RabbitMQHelper
import json

app = FastAPI()

def callback(ch, method, properties, body):

    body =  json.loads(body.decode('utf-8'))

    print(body)
    
def main():
    RabbitMQHelper.consume_message(callback = callback)

@app.on_event("startup")
def startup_event():
    main()

@app.get("/")
def root():
    return {"message": "Hello from backoffice"}