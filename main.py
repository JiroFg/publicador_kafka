from dotenv import load_dotenv
from kafka_publisher import KafkaPublisher
from confluent_kafka import KafkaException
import os

load_dotenv()

def main():
    print("##### Kafka Publisher #####")
    try:
        topics = eval(os.getenv("TOPICS_PUBLICA"))
        while True:
            print("A que topic desea publicar?")
            for index, topic in enumerate(topics):
                print(f"{index}. {topic}")
            selected_topic = int(input())
            print("Ingrese el mensaje que desea publicar:")
            msg = input()
            kafka_publisher = KafkaPublisher(topics)
            try:
                kafka_publisher.publish_message(selected_topic, msg)
                print("Mensaje publicado correctamente")
            except KafkaException as exception:
                print("Error al publicar el mensaje")
            print("Desea publicar otro mensaje? Y/N")
            repeat = input()
            if repeat == "N" or repeat == "n":
                raise KeyboardInterrupt
    except KeyboardInterrupt as e:
        pass

if __name__ == "__main__":
    main()