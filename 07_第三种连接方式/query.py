from db_init import Session, Person

session = Session()

# 普通查询
# result = session.query(Person).all()
# for person in result:
#     print(person.name)

# 带条件的查询
result = session.query(Person).filter(Person.address == 'aaa')

for person in result:
    print(person.name)

