from sqlalchemy import create_engine
from ..model.entities import Base

engine = create_engine('postgresql+psycopg2://postgres:123123@localhost/mydatabase', echo=True)
Base.metadata.create_all(engine)
