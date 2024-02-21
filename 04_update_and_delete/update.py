from db_init import engine, person_table

with engine.connect() as conn:
    # 不带条件
    # update_query = person_table.update().values(address='aaa')
    # 带条件
    update_query = person_table.update().values(address='bbb').where(person_table.c.id == 6 )
    conn.execute(update_query)
    conn.commit()
