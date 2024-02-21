import sqlalchemy

from db_init2 import engine, department, employee

with engine.connect() as conn:
    join = employee.join(department, department.c.id == employee.c.department_id)
    query = sqlalchemy.select(join).where(department.c.name == 'HR')
    query2 = sqlalchemy.select(employee).select_from(join).where(department.c.name == "HR")  # 意味着消除重复数据
    query3 = sqlalchemy.select(department).select_from(join).where(employee.c.name == "Mary")  # 同样的效果

    result = conn.execute(query)
    result2 = conn.execute(query2)
    result3 = conn.execute(query3)

    print(result.fetchall())
    print(result2.fetchall())
    print(result3.fetchall())
