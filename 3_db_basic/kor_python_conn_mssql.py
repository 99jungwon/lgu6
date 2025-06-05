"""
Connects to a SQL database using pymssql
"""

import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    port=1433,
    user='seo',
    password='1234',
    database='lily_book',
    charset='CP949',                # 한글 인코딩 처리 
    as_dict=True
)  

SQL_QUERY = """
SELECT employee_id, employee_name FROM staff;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r['employee_id']}\t{r['employee_name']}")