from db_init2 import engine, department, employee

with engine.connect() as conn:
    conn.execute(department.insert(), [
        {"name": "HR"}, {"name": "IT"}
    ])

    conn.execute(employee.insert(), [
        {"department_id": 1, 'name': 'jack'},
        {"department_id": 1, 'name': 'Tom'},
        {"department_id": 1, 'name': 'Mary'},
        {"department_id": 2, 'name': 'SSS'},
        {"department_id": 2, 'name': 'DDD'},
        {"department_id": 2, 'name': 'FFF'},
    ])
    conn.commit()
