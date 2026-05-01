

from stateInterface import OrderState


class PendingState(OrderState):
    def confirm(self, order):
        print("Order confirmed! Payment Receieved")
        order.state = ConfirmedState()

    def ship(self, order):
        print("Can't ship - confirm first!")

    def deliver(self, order):
        print("Cannot deliver- not shipped!")

    def cancel(self, order):
        print("Order cancelled. No charges")
        order.state = CancelledState()


class ConfirmedState(OrderState):
    def confirm(self, order):
        print("Already confirmed")

    def ship(self, order):
        print('Order shipped! Tracking ID assigned')
        order.state = ShippedState()

    def deliver(self, order):
        print("Cannot deliver- not yet shipped!")

    def cancel(self, order):
        print("Order cancelled. Refund Initiated")
        order.state = CancelledState()


class ShippedState():
    def confirm(self, order):
        print("Already confirmed")

    def ship(self, order):
        print('Already Shipped')

    def deliver(self, order):
        print("Order Delivered Successfully!")
        order.state = DeliveredState()

    def cancel(self, order):
        print("Cann't cancel - already Shipped!")


class DeliveredState():
    def confirm(self, order):
        print("Order completed")

    def ship(self, order):
        print('Order completed')

    def deliver(self, order):
        print("Already Shipped!")

    def cancel(self, order):
        print("Cann't cancel - Already Shipped!")


class CancelledState():
    def confirm(self, order):
        print("Order is Cancelled")

    def ship(self, order):
        print("Order is Cancelled")

    def deliver(self, order):
        print("Order is Cancelled")

    def cancel(self, order):
        print("Already Cancelled")
