import copy

from .entities import *
from copy import deepcopy
# Interface for db
class Db:
    def find_user(self, user_id: str) -> User:
        pass

    def find_order(self, order_id: str) -> Order:
        pass

    def find_pizza(self, pizza_id: str) -> Pizza:
        pass

    def find_topping(self, topping_id: str):
        pass

    def find_base_pizza(self, base_pizza_id: str) -> BasePizza:
        pass

    def add_user(self, user: User):
        pass

    def save_order(self, order: Order):
        pass

    def save_topping(self, topping: Topping):
        pass

    def save_base_pizza(self, base_pizza: BasePizza):
        pass


class InMemDb(Db):
    def __init__(self):
        self.users = dict()
        self.orders = dict()
        self.pizzas = dict()
        self.base_pizzas = dict()
        self.toppings = dict()

    def find_user(self, user_id: str) -> User:
        return copy.deepcopy(self.users[user_id])

    def find_order(self, order_id: str) -> Order:
        return copy.deepcopy(self.orders[order_id])

    def find_pizza(self, pizza_id: str) -> Pizza:
        return copy.deepcopy(self.pizzas[pizza_id])

    def find_topping(self, topping_id: str) -> Topping:
        return copy.deepcopy(self.toppings[topping_id])

    def find_base_pizza(self, base_pizza_id: str) -> BasePizza:
        return copy.deepcopy(self.base_pizzas[base_pizza_id])

    def add_user(self, user: User):
        self.users[user.user_id] = user

    def save_order(self, order: Order):
        self.orders[order.order_id] = order

    def save_topping(self, topping: Topping):
        self.toppings[topping.topping_id] = topping

    def save_base_pizza(self, base_pizza: BasePizza):
        self.base_pizzas[base_pizza.base_pizza_id] = base_pizza

    def save_pizza(self, pizza: Pizza):
        self.pizzas[pizza.pizza_id] = pizza
