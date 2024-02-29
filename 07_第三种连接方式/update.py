from db_init3 import Session, Person

session = Session()


# 第一种方法
person = session.query(Person).filter(Person.id == 1).one()
print(person.address)
print("------------对比---------------")
person.address = "www"
print(person.address)

print("------------对比---------------")
# 第二种方法
session.query(Person).filter(Person.id == 1).update(
    {
        Person.address : "PPP"
    }
)

print(person.name)

session.commit()