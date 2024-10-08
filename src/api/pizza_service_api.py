from fastapi import FastAPI
from ..service.pizza_service import PizzaService
from ..model.entities import Order, User, Pizza, OrderStatus
from ..model.db import InMemDb

app = FastAPI()

db = InMemDb()
pizza_service = PizzaService(db)


@app.post("/order/")
async def create_order(user_id: str):
    return pizza_service.create_order(user_id=user_id)


@app.get("/order/")
async def calc_price(order_id: str):
    return pizza_service.calc_price(order_id=order_id)


@app.put("/order/payment/")
async def on_payment_complete(order_id: str):
    return pizza_service.on_payment_complete(order_id=order_id)


@app.put("/order/status/")
async def update_order_status(order_id: str, status: OrderStatus):
    return pizza_service.update_order_status(order_id=order_id, status=status)


@app.post("/user/")
async def add_user(name: str, phone_number: int):
    return pizza_service.add_user(name=name, phone_number=phone_number)


@app.put("/user/{order_id}")
async def update_address(order_id: str, address: str):
    return pizza_service.update_address(order_id=order_id, address=address)


@app.post("/pizza/")
async def add_pizza(order_id: str, pizza: Pizza):
    return pizza_service.add_pizza(order_id=order_id, pizza=pizza)


@app.delete("/pizza/{pizza_id}")
async def remove_pizza(order_id: str, pizza_id: str):
    return pizza_service.remove_pizza(order_id=order_id, pizza_id=pizza_id)
