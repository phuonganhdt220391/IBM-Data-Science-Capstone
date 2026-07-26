import sqlite3
import pandas as pd

# Kết nối cơ sở dữ liệu SQLite
conn = sqlite3.connect('spacex.db')
cursor = conn.cursor()

# Truy vấn các bãi phóng duy nhất
query1 = "SELECT DISTINCT Launch_Site FROM spacex_table;"
df_sites = pd.read_sql(query1, conn)
print("Launch Sites:", df_sites)

# Truy vấn tổng khối lượng payload
query2 = "SELECT SUM(PAYLOAD_MASS__KG_) FROM spacex_table;"
total_payload = pd.read_sql(query2, conn)
print("Total Payload Mass:", total_payload)

conn.close()