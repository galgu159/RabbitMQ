import pika


def publisher():
    # The physical connection to the RabbitMQ server.
    connections = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # Creates a new virtual channel
    channel = connections.channel()
    # Create a queue named 'ABC'
    channel.queue_declare(queue='ABC')
    # Send 10 messages to the 'ABC' queue
    for i in range(10):
        message = f'Message number {i+1}'
        channel.basic_publish(exchange='', routing_key='ABC', body=message)
        print(f'Sent: {message}')

    # Close the connection
    connections.close()


if __name__ == '__main__':
    publisher()
