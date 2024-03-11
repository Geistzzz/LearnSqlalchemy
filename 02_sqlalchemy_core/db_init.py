import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:Zc.1319119251@localhost:3306/testdb", echo=True)

meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "persosn", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("addressss", sqlalchemy.String(255), nullable=True),
)

meta_data.create_all(engine)  # 重要：会确认你到底有没有这张表 有：不创建 没有：创建 # 不会创建重复的表 只会创建新表

# 插入一条记录
# insert_query = person.insert() # 这是生成语句
# insert_query = insert_query.values(name="Tom",birthday="2000-10-10") # 这是插入具体的数据

# 优化后的语句
# with engine.connect() as conn:
#     conn.execute(insert_query)
#     conn.commit()

# 一次性插入多条记录
# person_insert = person_table.insert()
# with engine.connect() as conn:
#     conn.execute(person_insert, [
#         {"name": "jack", "birthday": "2000-10-10"},
#         {"name": "Marry", "birthday": "2001-10-10"},
#         {"name": "Adam", "birthday": "2002-10-10"},
#     ])
#     conn.commit()


# 最新的改动
