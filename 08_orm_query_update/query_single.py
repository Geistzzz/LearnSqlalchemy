from db_init3 import Session, Person

session = Session()



# 循环查询
result = session.query(Person).filter(Person.address == 'aaa')

for person in result:
    print(person.name)

print("-------对比------------")
# 只查询第一条记录
result = session.query(Person).filter(Person.address == 'aaa').first()
print(result.name)
   
# 结果集里面只有一条记录one(),如果有多条数据会报错，没有数据也会报错
# 结果集里面只有一条记录scalar(),如果有多条数据会报错，没有数据不会报错



