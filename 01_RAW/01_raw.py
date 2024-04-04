from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://root:Zc.1319119251@127.0.0.1:3306/testdb")

sql = text("select * from cookies")

conn = engine.connect()
result = conn.execute(sql)


for row in result:
    print(row)

conn.close()
engine.dispose()

