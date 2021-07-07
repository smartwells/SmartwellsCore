import random
import time
import boto3
import _datetime

from paho.mqtt import client as mqtt_client

#функция отправки сообщений в YMQ
def toYMQ(message):
    #добавление к сообщению даты и времени
    d = _datetime.datetime.now()
    d = d.strftime('%Y%m%d%H%M%S')
    message = message[0] + '\"dt\":' + d + ',\n' + message[1:]

    # Create client
    client = boto3.client(
        service_name='sqs',
        endpoint_url='https://message-queue.api.cloud.yandex.net',
        region_name='ru-central1'
    )

    # Create queue and get its url
#    queue_url = client.create_queue(QueueName='sample-queue').get('QueueUrl')
#    print('Created queue url is "{}"'.format(queue_url))

    # Send message to queue
    queue_url='https://message-queue.api.cloud.yandex.net/b1gvrkfc5lbadse8lj14/dj6000000001ussf05n6/sample-queue'
    client.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print('Successfully sent test message to queue: "{}"'.format(message))

    # Receive sent message
#    messages = client.receive_message(
#        QueueUrl=queue_url,
#        MaxNumberOfMessages=10,
#        VisibilityTimeout=60,
#        WaitTimeSeconds=20
#    ).get('Messages')
#    for msg in messages:
#        print('Received message: "{}"'.format(msg.get('Body')))

    # Delete processed messages
#    for msg in messages:
#        client.delete_message(
#            QueueUrl=queue_url,
#            ReceiptHandle=msg.get('ReceiptHandle')
#        )
#        print('Successfully deleted message by receipt handle "{}"'.format(msg.get('ReceiptHandle')))

    # Delete queue
#    client.delete_queue(QueueUrl=queue_url)
#    print('Successfully deleted queue')
#конец функции

#настройки подключения к mosquitto
broker = 'localhost'
port = 1883
topic = "test"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'test'
password = '16551655'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #отправка в YMQ
        toYMQ(msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
