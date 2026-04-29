

from complexCode import *


class OrderFacade:
    def __init__(self):
        self._user = UserService()
        self._inventory = InventoryService()
        self._payment = PaymentService()
        self._orders = OrderService()
        self._notif = NotificationService()

    def placeOrder(self, user_id: int, item_id: int, amount: float):
        user = self._user.get_userid(user_id)

        if not self._inventory.checkStock(item_id):
            raise Exception("Out Of Stock")

        self._inventory.reserve_stock(item_id)
        txn = self._payment.charge(user_id, amount)
        order = self._orders.createOrder(user_id, item_id, txn)
        self._notif.send_confirmation(user_id, order)
        return order


facade = OrderFacade()
order = facade.placeOrder(user_id=1, item_id=24, amount=25.00)
print(f'Order Place:{order['order_id']}')
