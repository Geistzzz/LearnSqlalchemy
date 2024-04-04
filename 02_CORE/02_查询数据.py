from sqlalchemy import select, create_engine, Table, Column, MetaData, Integer, String, DateTime, Numeric, Float

engine = create_engine("mysql+pymysql://root:Zc.1319119251@127.0.0.1:3306/testdb")
metadata = MetaData()
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )
# metadata.create_all(bind=engine)
conn = engine.connect()
s = select(cookies)
rp = conn.execute(s)
results = rp.fetchall()
for row in results:
    print(row)
