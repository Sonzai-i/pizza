from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from ..model.entities import Pizza, OrderStatus, User, Order, BasePizza, Topping
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:123123@localhost/mydatabase', echo=True)
meta = MetaData()
conn = engine.connect()



meta.create_all(engine)
