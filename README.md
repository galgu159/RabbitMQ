# RabbitMQ
Implementing a Publisher and Consumer with Python using a Message Queue
step before running the codes :
# update 
sudo apt-get update
# install RabbitMQ server
sudo apt-get install rabbitmq-server
# enable RabbitMQ
sudo systemctl enable rabbitmq-server
# startRabbitMQ
sudo systemctl start rabbitmq-server
# see the server status
sudo systemctl status rabbitmq-server
 # enables the RabbitMQ Management Plugin
sudo rabbitmq-plugins enable rabbitmq_management
# enter to web ui in my browser 
https://http://localhost:15672
# username and password : guest
# install pika - communication between different parts of an application by sending and receiving messages.
pip install pika
# run consumer.py
python consumer.py
# run publisher.py
python3 publisher.py