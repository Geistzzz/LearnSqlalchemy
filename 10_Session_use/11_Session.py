from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎，session连接数据库需要
my_engine = create_engine('mysql+pymysql://root:123456@localhost/my_db')

# 创建一个配置过的Session类
Session = sessionmaker(bind=my_engine)

# 实例化一个session
db_session = Session()

# 使用session
myobject = MyObject('foo', 'bar')
db_session.add(myobject)
db_session.commit()