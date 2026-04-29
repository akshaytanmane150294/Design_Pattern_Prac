

class UserService:
    def get_userid(self, user_id: int):
        print(f'Fectching user id {user_id}')
        return {"id": user_id, 'name': "Alice"}


class InventoryService:
    def checkStock(self, item_id: int):
        print(f'Checking stock for item {item_id}')
        return True

    def reserve_stock(self, item_id: int):
        print(f'Stock reserve stock for item {item_id}')


class PaymentService:
    def charge(self, user_id: int, amount: float):
        print(f'Charging user {user_id} for {amount}')
        return 'Txn_112'


class OrderService:
    def createOrder(self, user_id: int, item_id: int, txn: str):
        print(f'Order created')
        return {'order_id': 'ORD_456', 'txn': txn}


class NotificationService:
    def send_confirmation(self, user_id: int, order: dict):
        print(f'Confirmation sent to user {user_id}')
