import os
from typing import Callable
import pika

from dotenv import load_dotenv


# env. file loaded
load_dotenv()

class RabbitMQHelper:

    QUEUE_NAME = "product_queue"

    def __init__(self) -> None:

        url = os.environ["RABBITMQ_URL"]
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(url))

        def __create_channel(self) -> pika.BlockingConnection:
            channel = self.__connection.channel()
            return channel
    
    def __create_queue(self) -> None:
        channel = self.__create_channel()
        channel.queue_declare(queue=self.QUEUE_NAME)

    def consume_message(self, callback: Callable) -> None:

        self.__create_queue()

        channel = self.__create_channel()
        channel.basic_consume(
            self.QUEUE_NAME,
            callback,
            auto_ack=True
        )

        channel.start_consuming()
        self.connection.close()

rabbitmq: RabbitMQHelper = RabbitMQHelper()