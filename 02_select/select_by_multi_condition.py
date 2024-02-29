from db_init import engine, person_table
from sqlalchemy import and_, or_

with engine.connect() as conn:
    query = person_table.select().where(
        or_(
            person_table.c.name == "Tom",
            and_(
                person_table.c.birthday > "2000-10-13",
                person_table.c.id < 7
            )
        )
    )
    result = conn.execute(query)

    print(result.fetchall())
