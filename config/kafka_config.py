import os
from dotenv import load_dotenv

load_dotenv()

configproducer = {
    'bootstrap.servers': os.getenv("KAFKA_HOST", default='example:9092'),
    'client.id': os.getenv("KAFKA_CLIENT", default='python-producer'),
}