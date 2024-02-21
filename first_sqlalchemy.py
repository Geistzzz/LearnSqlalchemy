import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:abcd=1234@localhost:3306/itcast")

conn = engine.connect()

query = sqlalchemy.text("select * from employee")

result = conn.execute(query)

for row_set in result:
    print(row_set)

conn.close()
engine.dispose()
