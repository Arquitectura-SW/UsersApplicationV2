import pika
import json
import datetime

rabbit_host = '10.128.0.12'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']


def log(document: str, level: str, message: str):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='topic')

        for topic in topics:
            payload = {
                'level': level,
                'message': message,
                'user': document,
                'timestamp': datetime.datetime.now().isoformat(),
            }
            message = json.dumps(payload)
            channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")

            
        
        
        
