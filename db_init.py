import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:abcd=1234@localhost:3306/itcast")

meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True),
)

meta_data.create_all(engine)

# 插入一条记录
# insert_query = person.insert().values(name="Tom",birthday="2000-10-10")
#
# with engine.connect() as conn:
#     conn.execute(insert_query)
#     conn.commit()

# 一次性插入多条记录
# person_insert = person_table    .insert()
# with engine.connect() as conn:
#     conn.execute(person_insert, [
#         {"name": "jack", "birthday": "2000-10-10"},
#         {"name": "Marry", "birthday": "2001-10-10"},
#         {"name": "Adam", "birthday": "2002-10-10"},
#     ])
#     conn.commit()
