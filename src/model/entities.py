from enum import Enum
from typing import List

class OrderStatus(Enum):
    NEW = 1
    ORDERED = 2
    PREPARING = 3
    READY = 4
    DELIVERING = 5
    DELIVERED = 6
    COMPLETED = 7

class User:
    pass

class Order:
    pass

class BasePizza:
    pass

class Pizza:
    def __init__(self, pizza_id: str, base_pizza_id: str, topping_ids: List[str]):
        self.pizza_id = pizza_id
        self.base_pizza_id = base_pizza_id
        self.topping_ids = topping_ids

class Topping:
    pass
