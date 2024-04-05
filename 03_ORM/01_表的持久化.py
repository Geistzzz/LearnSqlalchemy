from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))


engine = create_engine("mysql+pymysql://root:Zc.1319119251@127.0.0.1:3306/testdb")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
