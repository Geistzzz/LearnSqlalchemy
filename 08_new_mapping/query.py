from db_init4 import Session, Customer

session = Session()

c = Customer(name='AAA', birthday='2000-01-05')  # 实例化一个对象

session.add(c)  # 添加到这个表里面

session.commit()
