import sqlite3

conn = sqlite3.connect('fun_facts_database.db')
print("opened database successfully")
#conn.execute('Drop TABLE facts')
conn.execute('CREATE TABLE facts (name TEXT, fact TEXT);')
print("Table created successfully")

conn = sqlite3.connect('restaurant_database.db')
print("opened database successfully")
#conn.execute('Drop TABLE facts')
conn.execute('CREATE TABLE restaurants (email TEXT, name TEXT, location TEXT);')
print("Table created successfully")

conn.close()
