# 第一步倒入sqlalchemy
import sqlalchemy
# 创建数据库引擎
engine = sqlalchemy.create_engine("mysql+pymysql://root:Zc.1319119251@localhost:3306/testdb")
# 建立连接
conn = engine.connect()
# 之后可以进行查询，等一些列的操作
query = sqlalchemy.text("select * from student")
result = conn.execute(query)
for row_set in result:
    print(row_set)
# 关闭连接，关闭引擎
conn.close()
engine.dispose()
