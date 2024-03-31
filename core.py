# -*- coding = utf-8 -*-
# @Time : 2024/3/28 23:49
# @Author : Geist
# @File ： core.py
# @Software: PyCharm

from datetime import datetime
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, String, Numeric, ForeignKey, DateTime, Boolean, Float

metadata = MetaData()

cookies = Table('cookies', metadata,  # 普通表
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),  # 可以加快该列的查询速度
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))
orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),
               Column('shipped', Boolean(), default=False))
line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order_id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )
engine = create_engine('sqlite:///:memory:')
metadata.create_all(engine)

# Table对象有自己的insert方法
ins = cookies.insert().values(
                             cookie_name="chocolate chip",
                             cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
                             cookie_sku="CC01",
                             quantity="12",
                             unit_cost="0.50"
                            )
result = connection.execute(ins)

# insert语句也可以单独使用
from sqlalchemy import insert
ins = insert(cookies).values(
 cookie_name="chocolate chip",
 cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
 cookie_sku="CC01",
 quantity="12",
 unit_cost="0.50"
)
# 可以使用字典一次性插入多条记录
inventory_list = [
 {
 'cookie_name': 'peanut butter',
'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
 'cookie_sku': 'PB01',
 'quantity': '24',
 'unit_cost': '0.25'
 },
 {
 'cookie_name': 'oatmeal raisin',
 'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
 'cookie_sku': 'EWW01',
 'quantity': '100',
 'unit_cost': '1.00'
 }
]
result = connection.execute(ins, inventory_list)
# 查询函数
from sqlalchemy.sql import select
s = select([cookies])
rp = connection.execute(s)
results = rp.fetchall()

# 另一种查询函数
from sqlalchemy.sql import select
s = cookies.select()
rp = connection.execute(s)
results = rp.fetchall()