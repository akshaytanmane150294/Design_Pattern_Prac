

class StripeAPI:
    def makeTransaction(self, value, currency="USD"):
        return f"stripe_txn_{value}"


class RazorPayAPI:
    def pay_now(self, amount, currency="INR"):
        return f"razorpay_txn_{amount}"
