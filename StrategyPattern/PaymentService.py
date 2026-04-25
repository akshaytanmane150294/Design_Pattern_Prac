
from PaymentStrategy import PaymentStrategy
from Providers import *


class PaymentServices:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def setStrategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def processPayment(self, amount: float):
        self.strategy.pay(amount)


service = PaymentServices(UPIpayment())
service.processPayment(1000)

service = PaymentServices(CardPayment())
service.setStrategy(CardPayment())

service.processPayment(1200)

service = PaymentServices(CriptoBit())
service.processPayment(1300)
