from .service.pizza_service import PizzaService
from .model.db import InMemDb
from .model.entities import *
from typing import List
import uuid

def deliver_order(pizza_service: PizzaService, order_id: str):
    # TODO: add asserts 
    # TODO: fix

    statuses = [
        OrderStatus.PREPARING,
        OrderStatus.READY,
        OrderStatus.DELIVERING,
        OrderStatus.DELIVERED
    ]
    for status in statuses:
        pizza_service.update_order_status(order_id, status)


def test_pizza_sevice_happy_path():
    # TODO: add asserts 
    # TODO: fix

    db = InMemDb()
    
    pepperoni = BasePizza(base_pizza_id=str(uuid.uuid4()),
                          name='Пеперони',
                          description='Пряные колбаски пепперони с легкой перчинкой, '
                                      'сыр моцарелла со сливочным вкусом и нежный томатный соус',
                          price_rub= 1280)
    db.save_base_pizza(pepperoni)

    pinapple = Topping(topping_id=str(uuid.uuid4()),
                       name='Ананасы',
                       description='Сочные нарезанные кусочки ананаса!',
                       price_rub= 60)
    db.save_topping(pinapple)

    pepperoni_pinapple = Pizza(
        str(uuid.uuid4()),
        pepperoni.base_pizza_id,
        [pinapple.topping_id]
    )
    db.save_pizza(pepperoni_pinapple)

    pizza_service = PizzaService(db)
    user = pizza_service.add_user("Name", 79003002010)
    order = pizza_service.create_order(order_id=str(uuid.uuid4()),
                                       user_id=user.user_id,
                                       pizza_ids=[],
                                       address='')

    pizza_service.add_pizza(order.order_id, pepperoni_pinapple)
    pizza_service.update_address(order.order_id, 'Russia, Moscow, Krasnaya ploschad, 1')
    
    pizza_service.update_order_status(order.order_id, OrderStatus.ORDERED)
    deliver_order(pizza_service=pizza_service, order_id=order.order_id)
    price = pizza_service.calc_price(order.order_id)
    # TODO: validate price

    pizza_service.on_payment_complete(order.order_id)
    pizza_service.update_order_status(order.order_id, OrderStatus.COMPLETED)

