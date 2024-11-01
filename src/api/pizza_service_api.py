from typing import List
from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel
from sqlalchemy import create_engine

from ..service.pizza_service import PizzaService
from ..model.entities import Pizza, OrderStatus, Base, User
from ..model.db import SqlDb

app = FastAPI()
router = APIRouter()
engine = create_engine('postgresql+psycopg2://postgres:123123@localhost/mydatabase', echo=True)
Base.metadata.create_all(engine)

db = SqlDb(engine)
pizza_service = PizzaService(db)


class PizzaModel(BaseModel):
    pizza_id: str
    base_pizza_id: str
    topping_ids: List[str]

    def to_pizza(self) -> Pizza:
        return Pizza(
            pizza_id=self.pizza_id,
            base_pizza_id=self.base_pizza_id,
            topping_ids=self.topping_ids
        )


@router.post("/order/")
async def create_order(user_id: str):
    return pizza_service.create_order(user_id=user_id)


@router.get("/order/")
async def calc_price(order_id: str):
    return pizza_service.calc_price(order_id=order_id)


@router.put("/order/payment/")
async def on_payment_complete(order_id: str):
    return pizza_service.on_payment_complete(order_id=order_id)


@router.put("/order/status/")
async def update_order_status(order_id: str, status: int = Query(..., ge=1, le=7)):
    return pizza_service.update_order_status(order_id=order_id, status=OrderStatus(status))


@router.post("/user/")
async def add_user(name: str, phone_number: int):
    return pizza_service.add_user(name=name, phone_number=phone_number)


@router.post("/user/{order_id}")
async def update_address(order_id: str, address: str):
    return pizza_service.update_address(order_id=order_id, address=address)


@router.post("/pizza/")
async def add_pizza(order_id: str, pizza_model: PizzaModel):
    pizza = pizza_model.to_pizza()
    return pizza_service.add_pizza(order_id=order_id, pizza=pizza)


@router.delete("/pizza/{pizza_id}")
async def remove_pizza(order_id: str, pizza_id: str):
    return pizza_service.remove_pizza(order_id=order_id, pizza_id=pizza_id)


app.include_router(router)
