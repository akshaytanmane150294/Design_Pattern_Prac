
from Subscriber import *


class Broker:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topic, service):
        self.topics.setdefault(topic, []).append(service)

    def publish(self, topic, data):
        for service in self.topics.get(topic, []):
            service.update(data)


broker = Broker()

broker.subscribe("Order.placed", EmailService())
broker.subscribe("Order.placed", SMSService())
broker.publish("Order.placed", {'id': 1234, 'amount': 500})
