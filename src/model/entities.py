import uuid
from enum import Enum
from typing import List
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OrderStatus(Enum):
    NEW = 1
    ORDERED = 2
    PREPARING = 3
    READY = 4
    DELIVERING = 5
    DELIVERED = 6
    COMPLETED = 7


class User(Base):
    __tablename__ = 'User'

    def __init__(self, name: str, phone_number: int, user_id: str):
        self.name = name
        self.phone_number = phone_number
        self.user_id = user_id


class Order(Base):
    __tablename__ = 'Order'

    def __init__(self, user_id: str):
        self.order_id = str(uuid.uuid4())
        self.user_id = user_id
        self.pizza_ids = []
        self.order_status = OrderStatus.NEW
        self.paid = False
        self.address = ''


class BasePizza(Base):
    __tablename__ = 'BasePizza'

    def __init__(self, base_pizza_id: str, name: str, description: str, price_rub: float):
        self.base_pizza_id = base_pizza_id
        self.name = name
        self.description = description
        self.price_rub = price_rub


class Pizza(Base):
    __tablename__ = 'Pizza'

    def __init__(self, pizza_id: str, base_pizza_id: str, topping_ids: List[str]):
        self.pizza_id = pizza_id
        self.base_pizza_id = base_pizza_id
        self.topping_ids = topping_ids


class Topping(Base):
    __tablename__ = 'Topping'

    def __init__(self, topping_id: str, name: str, description: str, price_rub: float):
        self.topping_id = topping_id
        self.name = name
        self.description = description
        self.price_rub = price_rub
