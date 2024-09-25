from typing import List

from ..model.entities import Order, User, Pizza, OrderStatus
from ..model.db import Db
from uuid import uuid4


class PizzaService:
    next_status = {
        OrderStatus.NEW: OrderStatus.ORDERED,
        OrderStatus.ORDERED: OrderStatus.PREPARING,
        OrderStatus.PREPARING: OrderStatus.READY,
        OrderStatus.READY: OrderStatus.DELIVERING,
        OrderStatus.DELIVERING: OrderStatus.DELIVERED,
        OrderStatus.DELIVERED: OrderStatus.COMPLETED
    }

    def __init__(self, db: Db):
        self.db = db

    def create_order(self, order_id: str, user_id: str, pizza_ids: List[str], address: str ) -> Order:
        order = Order(user_id=user_id, order_id=order_id, pizza_ids=pizza_ids, address=address)
        self.db.save_order(order)
        return order

    def add_user(self, name: str, phone_number: int) -> User:
        user = User(name=name,
                    phone_number=phone_number,
                    user_id=str(uuid4()))

        self.db.add_user(user)
        return user

    def add_pizza(self, order_id: str, pizza: Pizza):
        status_for_order = {
            OrderStatus.NEW: OrderStatus.ORDERED,
            OrderStatus.ORDERED: OrderStatus.ORDERED,
        }
        order = self.db.find_order(order_id)
        assert order.order_status in status_for_order
        order.pizza_ids.append(pizza.pizza_id)
        order.order_status = status_for_order[order.order_status]
        self.db.save_order(order)

    def remove_pizza(self, order_id: str, pizza_id: str):
        order = self.db.find_order(order_id)
        assert order.order_status == OrderStatus.ORDERED
        assert pizza_id in order.pizza_ids
        order.pizza_ids.remove(pizza_id)
        self.db.save_order(order)

    def update_address(self, order_id: str, address: str):
        order = self.db.find_order(order_id)
        order.address = address
        self.db.save_order(order)

    def calc_price(self, order_id: str) -> float:
        order = self.db.find_order(order_id)
        sum_order = 0.0
        for pizza_id in order.pizza_ids:
            pizza = self.db.find_pizza(pizza_id)
            sum_order += self._calc_price_pizza(pizza)
            sum_order += self._calc_price_topping(pizza)
        return sum_order

    def _calc_price_pizza(self, pizza: Pizza) -> float:
        baze_pizza_id = self.db.find_base_pizza(pizza.base_pizza_id)
        return baze_pizza_id.price_rub

    def _calc_price_topping(self, pizza: Pizza) -> float:
        topping_ids = pizza.topping_ids
        sum_ = 0
        for _ in topping_ids:
            topping = self.db.find_topping(_)
            sum_ += topping.price_rub
        return sum_

    def on_payment_complete(self, order_id: str):
        order = self.db.find_order(order_id)
        order.paid = True
        self.db.save_order(order)


    def update_order_status(self, order_id: str, status: OrderStatus):
        order = self.db.find_order(order_id)
        assert order.order_status in self.next_status
        assert status == self.next_status[order.order_status]
        if status == OrderStatus.COMPLETED:
            assert order.paid

        order.order_status = status
        self.db.save_order(order)

