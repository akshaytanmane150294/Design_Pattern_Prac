

from stateInterface import *
from concreateClass import *

# Context class


class Order:
    def __init__(self, orderid: str):
        self.orderid = orderid
        self.state = PendingState()

    def confirm(self):
        self.state.confirm(self)

    def ship(self):
        self.state.ship(self)

    def deliver(self):
        self.state.deliver(self)

    def cancel(self):
        self.state.cancel(self)

    def getState(self):
        return self.state.__class__.__name__


order = Order('Order001')

print(order.getState())
order.ship()

order.confirm()
order.ship()
order.cancel()

order.deliver()
print(order.getState())
