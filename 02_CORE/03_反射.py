from sqlalchemy import MetaData, create_engine

metadata = MetaData()
engine = create_engine("mysql+pymysql://root:Zc.1319119251@127.0.0.1:3306/testdb")
metadata.create_all(engine)

from sqlalchemy import Table

artist = Table('cookies', metadata, autoload_with=engine)

artist.columns.keys()
from sqlalchemy import select
s = select(artist).limit(10)
print(engine.connect().execute(s).fetchall())
