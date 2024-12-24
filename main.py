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
            try:
                selected_topic = get_topic(topics)
                msg = get_msg()
                publish_msg(topics, selected_topic, msg)
            except ValueError:
                print("Por favor ingrese un numero valido")
            repeat_menu()
    except KeyboardInterrupt as e:
        pass

def get_topic(topics):
    print("A que topic desea publicar?")
    for index, topic in enumerate(topics):
        print(f"{index}. {topic}")
    selected_topic = int(input())
    if selected_topic > len(topics)-1 or selected_topic < 0:
        raise ValueError
    return selected_topic

def get_msg():
    msg = ""
    while msg == "":
        print("Ingrese el mensaje que desea publicar:")
        msg = input()
    return msg

def publish_msg(topics, selected_topic, msg):
    kafka_publisher = KafkaPublisher(topics)
    try:
        kafka_publisher.publish_message(selected_topic, msg)
        print("Mensaje publicado correctamente")
    except KafkaException as exception:
        print("Error al publicar el mensaje")

def repeat_menu():
    invalid = True
    while invalid:
        print("Desea publicar otro mensaje? Y/N")
        repeat = input()
        if repeat == "N" or repeat == "n":
            raise KeyboardInterrupt
        elif repeat == "Y" or repeat == "y":
            invalid = False

if __name__ == "__main__":
    main()