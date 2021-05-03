import sqlite3

conn = sqlite3.connect('fun_facts_database.db')
print("opened database successfully")
#conn.execute('Drop TABLE facts')
#conn.execute('CREATE TABLE facts (name TEXT, fact TEXT);')
conn.execute('CREATE TABLE contact (name TEXT, email TEXT, problem TEXT, description TEXT);')
#conn.execute('INSERT INTO facts(name, fact) VALUES("Connor", "Boy do I like those crazy noodles");')
print("Table created successfully")

conn = sqlite3.connect('restaurant_database.db')
print("opened database successfully")
#conn.execute('Drop TABLE facts')
conn.execute('CREATE TABLE restaurants (email TEXT, name TEXT, location TEXT);')
print("Table created successfully")

conn.close()
