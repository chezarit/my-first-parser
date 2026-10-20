import sqlite3


create_products_table = """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL
    );
"""

create_price_history_table = """
    CREATE TABLE price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        price INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
"""

conn = sqlite3.connect('memory_prices.db')
cursor = conn.cursor()

cursor.execute(create_products_table) 
cursor.execute(create_price_history_table)

conn.commit()
conn.close()