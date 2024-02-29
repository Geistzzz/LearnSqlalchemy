import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:Zc.1319119251@localhost:3306/test")


conn = engine.connect()
#
query = sqlalchemy.text("select * from test")
#
result = conn.execute(query)
#
for row_set in result:
    print(row_set)

conn.close()
engine.dispose()
