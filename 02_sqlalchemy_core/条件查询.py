from db_init import engine, person_table

with engine.connect() as conn:
    query = person_table.select().where(person_table.c.birthday > "2000-10-13")
    result = conn.execute(query)

    print(result.fetchall())


