# -*- coding = utf-8 -*-
# @Time : 2024/3/3 23:10
# @Author : Geist
# @File ： pp.py
# @Software: PyCharm
import datetime

first_time = datetime.datetime.now()
for i in range(10000):
    user = User(username=username + str(i), password=password)
    db.session.add(user)
    db.session.commit()
second_time = datetime.datetime.now()
print((second_time - first_time).total_seconds())


second_time = datetime.utcnow()
db.session.bulk_save_objects(
    [
        User(username=username + str(i), password=password)
        for i in range(10000)
    ]
)
db.session.commit()
third_time = datetime.utcnow()
print((third_time - second_time).total_seconds())


third_time = datetime.utcnow()
db.session.bulk_insert_mappings(
    User,
    [
        dict(username="NAME INSERT " + str(i), password=password)
        for i in range(10000)
    ]
)
db.session.commit()
fourth_time = datetime.utcnow()
print((fourth_time - third_time).total_seconds())

fourth_time = datetime.utcnow()
db.session.execute(
    User.__table__.insert(),
    [{"username": 'Execute NAME ' + str(i), "password": password} for i in range(10000)]
)
db.session.commit()
five_time = datetime.utcnow()
print((five_time - fourth_time).total_seconds())