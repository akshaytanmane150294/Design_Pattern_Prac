
from PaymentStrategy import PaymentStrategy


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using Credit/debit card')


class UPIpayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using UPI')


class Paypal(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using Paypal')


class CriptoBit(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using Cripto')
