# -*- coding = utf-8 -*-
# @Time : 2024/3/30 12:36
# @Author : Geist
# @File ： orm.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref, declarative_base

from datetime import datetime
from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime, ForeignKey)

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer(),primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))


#
#
# class User(Base):
#     __tablename__ = 'users'
#     user_id = Column(Integer(), primary_key=True)
#     username = Column(String(15), nullable=False, unique=True)
#     email_address = Column(String(255), nullable=False)
#     phone = Column(String(20), nullable=False)
#     password = Column(String(25), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#
#
# class Order(Base):
#     __tablename__ = 'orders'
#     order_id = Column(Integer(), primary_key=True)
#     user_id = Column(Integer(), ForeignKey('users.user_id'))
#     user = relationship("User", backref=backref('orders', order_by=order_id))
#
#
# class LineItems(Base):
#     __tablename__ = 'line_items'
#     line_item_id = Column(Integer(), primary_key=True)
#     order_id = Column(Integer(), ForeignKey('orders.order_id'))
#     cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
#     quantity = Column(Integer())
#     extended_cost = Column(Numeric(12, 2))
#     order = relationship("Order", backref=backref('line_items', order_by=line_item_id))
#     cookie = relationship("Cookie", uselist=False, order_by=id)


engine = create_engine("mysql+pymysql://root:Zc.1319119251@localhost:3306/testdb")

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

dict = dict(
            cookie_id=1,
            cookie_name='多放点咯i结果',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
            cookie_sku='的萨法',
            quantity=5,
            unit_cost=0.50)

print([dict])
mappings = [Cookie(

            cookie_name='多放点咯i结果',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
            cookie_sku='的萨法',
            quantity=12,
            unit_cost=0.50),
            Cookie(

            cookie_name='多放点咯irrrrrr结果',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
            cookie_sku='的萨rr法',
            quantity=12,
            unit_cost=0.50),]
# session.add(cc_cookie)

# dcc = Cookie(cookie_name='dark chocolate chip',
#              cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
#              cookie_sku='CC02',
#              quantity=1,
#              unit_cost=0.75)
# mol = Cookie(cookie_name='molasses',
#              cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
#              cookie_sku='MOL01',
#              quantity=1,
#              unit_cost=0.80)
# session.add(dcc)
# session.add(mol)
# session.flush()
# print(dcc.cookie_id)
# print(mol.cookie_id)

result = session.query(Cookie)
result.delete()
# print(result)
session.bulk_insert_mappings(Cookie, [dict])
# print(1/0)


session.commit()
