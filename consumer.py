import pika


def callback(channel, method, properties, body):
    print(f"Received: {body.decode()}")


def consumer():
    # The physical connection to the RabbitMQ server.
    connections = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # Creates a new virtual channel
    channel = connections.channel()
    # Create or connect to the queue named 'ABC'
    channel.queue_declare(queue='ABC')
    # Subscribe to the 'ABC' queue, process messages and after delete the message
    channel.basic_consume(queue='ABC', on_message_callback=callback, auto_ack=True)

    print('Ready to receive message. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
