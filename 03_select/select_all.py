from db_init import engine, person_table

with engine.connect() as conn:
    query = person_table.select()
    result = conn.execute(query)

    # 一、用for循环
    # for row_set in result:
    #     print(row_set)

    # 二、全都打印出来
    # print(result.fetchall())

    # 三、只查询第一条记录
    # print(result.fetchone())
