from db_init5 import Session, Department, Employee


def insert_records(session):
    d1 = Department(name="HR")

    e1 = Employee(department=d1, name="Jack", birthday="2000-10-01")
    # 这里修改一下，相当于把部门这个属性，指向部门那个对象
    session.add(e1)  # 这个加进去的时候会产生连锁反应
    session.commit()


def select_employee(session):
    emp = session.query(Employee).filter(Employee.id == 1).one()

    print(emp)

    # print(emp.department)

def select_department(session):
    dep = session.query(Department).filter(Department.id == 1).one()

    print(dep)

    # print(emp.department)



session = Session()
# insert_records(session)
# select_employee(session)
select_department(session)
