from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
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

    def save_pizza(self, pizza: Pizza):
        pass


class InMemDb(Db):

    def __init__(self):
        self.users = dict()
        self.orders = dict()
        self.pizzas = dict()
        self.base_pizzas = dict()
        self.toppings = dict()

    def find_user(self, user_id: str) -> User:
        return deepcopy(self.users[user_id])

    def find_order(self, order_id: str) -> Order:
        return deepcopy(self.orders[order_id])

    def find_pizza(self, pizza_id: str) -> Pizza:
        return deepcopy(self.pizzas[pizza_id])

    def find_topping(self, topping_id: str) -> Topping:
        return deepcopy(self.toppings[topping_id])

    def find_base_pizza(self, base_pizza_id: str) -> BasePizza:
        return deepcopy(self.base_pizzas[base_pizza_id])

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


class SqlDb(Db):
    def __init__(self, engine):
        self.engine = create_engine(engine, echo=True)
        Base.metadata.create_all(self.engine)

    def find_user(self, user_id: str) -> User:
        with Session(self.engine) as session:
            stmt = select(User).where(user_id == User.user_id)
            return session.execute(stmt).one_or_none()[0]

    def find_order(self, order_id: str) -> Order:
        with Session(self.engine) as session:
            stmt = select(Order).where(order_id == Order.order_id)
            return session.execute(stmt).one_or_none()[0]

    def find_pizza(self, pizza_id: str) -> Pizza:
        with Session(self.engine) as session:
            stmt = select(Pizza).where(pizza_id == Pizza.pizza_id)
            return session.execute(stmt).one_or_none()[0]

    def find_topping(self, topping_id: str) -> Topping:
        with Session(self.engine) as session:
            stmt = select(Topping).where(topping_id == Topping.topping_id)
            return session.execute(stmt).one_or_none()[0]

    def find_base_pizza(self, base_pizza_id: str) -> BasePizza:
        with Session(self.engine) as session:
            stmt = select(BasePizza).where(base_pizza_id == BasePizza.base_pizza_id)
            return session.execute(stmt).one_or_none()[0]

    def add_user(self, user: User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

    def save_order(self, order: Order):
        with Session(self.engine) as session:
            stmt = insert(Order).values(
                order_id=order.order_id,
                user_id=order.user_id,
                pizza_ids=order.pizza_ids,
                order_status=order.order_status,
                paid=order.paid,
                address=order.address
            )
            stmt = stmt.on_conflict_do_update(
                constraint='Order_pkey',
                set_={
                    'pizza_ids': order.pizza_ids,
                    'order_status': order.order_status,
                    'paid': order.paid,
                    'address': order.address
                }
            )
            session.execute(stmt)
            session.commit()

    def save_topping(self, topping: Topping):
        with Session(self.engine) as session:
            session.add(topping)
            session.commit()

    def save_base_pizza(self, base_pizza: BasePizza):
        with Session(self.engine) as session:
            session.add(base_pizza)
            session.commit()

    def save_pizza(self, pizza: Pizza):
        with Session(self.engine) as session:
            session.add(pizza)
            session.commit()
