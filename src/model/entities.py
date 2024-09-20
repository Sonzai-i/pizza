import random
import uuid
from enum import Enum
from typing import List
from uuid import uuid4


class OrderStatus(Enum):
    NEW = 1
    ORDERED = 2
    PREPARING = 3
    READY = 4
    DELIVERING = 5
    DELIVERED = 6
    COMPLETED = 7

class User:
    def __init__(self, name: str, phone_number: int, user_id: str):
        self.name = name
        self.phone_number = phone_number
        self.user_id = user_id

class Order:
    def __init__(self, order_id: str, user_id: str, pizza_ids: List[str], order_status: OrderStatus, paid: bool):
        self.order_id = order_id
        self.user_id = user_id
        self.pizza_ids = pizza_ids
        self.order_status = order_status
        self.paid = paid

class BasePizza:
    alphabet = list(map(chr, range(97, 123)))
    def __init__(self):
        self.base_pizza_id = str(uuid.uuid4())
        self.name = ''.join(random.sample(self.alphabet, random.randint(4, 10)))
        self.description = ''
        self.price_rub = len(self.name) * 180

class Pizza:
    def __init__(self, pizza_id: str, base_pizza_id: str, topping_ids: List[str]):
        self.pizza_id = pizza_id
        self.base_pizza_id = base_pizza_id
        self.topping_ids = topping_ids

class Topping:
    alphabet = list(map(chr, range(97, 123)))
    def __init__(self):
        self.topping_id = str(uuid.uuid4())
        self.name = ''.join(random.sample(self.alphabet, random.randint(4, 10)))
        self.description = ''
        self.price_rub = len(self.name) * 9
