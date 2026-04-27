from ThirdPartyAPI import *
from paymentProcess import *


class StripeAdapter(PaymentProcess):
    def __init__(self):
        self._stripepay = StripeAPI()

    def pay(self, amount: float):
        return self._stripepay.makeTransaction(amount)


class RazorpayAdapter(PaymentProcess):
    def __init__(self):
        self._razorpay = RazorPayAPI()

    def pay(self, amount: float):
        return self._razorpay.pay_now(amount)


def process_checkout(processor: PaymentProcess, amount: float):
    txn_id = processor.pay(amount)
    print(f'Payment Successful:{txn_id}')


process_checkout(StripeAdapter(), 600.00)
process_checkout(RazorpayAdapter(), 800.00)
