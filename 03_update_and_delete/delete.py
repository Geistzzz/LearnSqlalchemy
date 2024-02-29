from db_init import engine, person_table

with engine.connect() as conn:
    # 不带条件
    # update_query = person_table.delete().values(address='aaa')
    # 带条件
    update_query = person_table.delete().where(person_table.c.id == 7)
    conn.execute(update_query)
    conn.commit()
