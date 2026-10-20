import sqlite3


conn = sqlite3.connect('memory_prices.db')
cursor = conn.cursor()

sql = "INSERT INTO products (name, url) VALUES (?, ?)"
cursor.execute(sql, ("Kingston fury 16GB",  "https://example.com/kingston"))

sql_price = "INSERT INTO price_history (product_id, price, date) VALUES (?, ?, ?)"
cursor.execute(sql_price, (1, 5000, "2026-10-21"))

conn.commit()
conn.close()