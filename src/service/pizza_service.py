from ..model.entities import Order, User, Pizza, OrderStatus
from ..model.db import Db
from uuid import uuid4

class PizzaService:
    def __init__(self, db: Db):
        self.db = db

    def create_order(self, user_id: str) -> Order:
        order = Order(order_id=str(uuid4()),
                     user_id=user_id,
                     pizza_ids=[],
                     order_status=OrderStatus.NEW,
                     paid=False)

        self.db.save_order(order)
        return order

    def add_user(self, name: str, phone_number: int) -> User:
        user = User(name=name,
                    phone_number=phone_number,
                    user_id=str(uuid4()))

        self.db.add_user(user)
        return user

    def add_pizza(self, order_id: str, pizza: Pizza):
        order = self.db.find_order(order_id)
        order.pizza_ids.append(pizza.base_pizza_id)

    def remove_pizza(self, order_id: str, pizza_id: str):
        order = self.db.find_order(order_id)
        order.pizza_ids.remove(pizza_id)

    def update_address(self, order_id: str):
        pass

    def calc_price(self, order_id: str) -> float:
        pass

    def on_payment_complete(self, order_id: str):
        pass
    
    def update_order_status(self, order_id: str, status: OrderStatus):
        # TODO: validate status
        # IMPORTANT: status can be updated only after validation
        pass


