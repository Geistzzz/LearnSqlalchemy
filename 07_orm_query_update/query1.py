from db_init3 import Session, Person

session = Session()

# 这是增加一条记录
# p = Person(name="Amy", birthday="2000-9-15", address="unknow")
# session.add(p)

# 这是增加多条记录
plist = [
    Person(name="Amc", birthday="2000-9-15", address="unknow"),
    Person(name="Bmc", birthday="2000-9-15", address="unknow"),
    Person(name="Bfc", birthday="2000-9-15", address="unknow")
]
session.add_all(plist)

session.commit()
