"""
Connects to a SQL database using pymssql
"""

import pymssql

conn = pymssql.connect(
    server='127.0.0.1',
    port=1433,
    user='seo',
    password='1234',
    database='BikeStores',
    as_dict=True, 
    char
)  

SQL_QUERY = """
SELECT * FROM production.brands;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r['brand_id']}\t{r['brand_name']}")