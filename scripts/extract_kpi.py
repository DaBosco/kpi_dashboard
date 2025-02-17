import pymysql
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="changeme",  
    database="kpi_db"
)

queries = {
    "total_sales": "SELECT SUM(revenue) FROM sales;",
    "total_orders": "SELECT COUNT(*) FROM sales;",
    "best_selling_product": "SELECT product FROM sales GROUP BY product ORDER BY SUM(units_sold) DESC LIMIT 1;"
}

kpi_data = {}
for kpi, query in queries.items():
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        kpi_data[kpi] = result[0] if result else None

df = pd.DataFrame([kpi_data])
df.to_csv("./data/kpi_report.csv", index=False)

print("✅ KPI Report Generated")

conn.close()
