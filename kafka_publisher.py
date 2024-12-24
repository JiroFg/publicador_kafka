from dotenv import load_dotenv
from confluent_kafka import Producer
from config.kafka_config import configproducer
import os

load_dotenv()

class KafkaPublisher:
    def __init__(self, topics):
        self.topics = topics
    
    def publish_message(self, selected_topic: int, msg: str):
        producer = Producer(configproducer)
        producer.produce(self.topics[selected_topic], value=msg)
        producer.flush()