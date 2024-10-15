from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from ..model.entities import Pizza, OrderStatus, User, Order, BasePizza, Topping, Base
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:123123@localhost/mydatabase', echo=True)

Base.metadata.create_all(engine)

