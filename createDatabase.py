import sqlite3

conn = sqlite3.connect('database.db')
print("opened database successfully")

conn.execute('CREATE TABLE facts (name TEXT, fact TEXT);')
conn.execute('INSERT INTO facts(name, fact) VALUES("Connor", "Boy do I like those crazy noodles");')
conn.commit()

conn.execute('CREATE TABLE contact (name TEXT, email TEXT, problem TEXT, description TEXT);')

conn.execute('CREATE TABLE restaurants (email TEXT, restaurant TEXT, address TEXT);')

conn.execute('CREATE TABLE recipes (email TEXT, recipe TEXT, link TEXT);')

print("Tables created successfully")

conn.close()
