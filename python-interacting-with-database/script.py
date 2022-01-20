import sqlite3

connectDb = sqlite3.connect("lite.db") # connect to database
curObj = connectDb.cursor() # make database connection object

# creating table
def create_table():
    curObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGEER, price REAL)")
    connectDb.commit()

# inserting data in table
def insert_entry(item, quantity, price):
    curObj.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    connectDb.commit()
    print("done")

# view entries in the database table
def view_entries():
    curObj.execute("SELECT * FROM store")
    entry = curObj.fetchall()
    
    return entry

# delete specific row
def delete_entry(item):
    curObj.execute("DELETE FROM store WHERE item = ?",(item,))
    connectDb.commit()

# update specific row
def update_entry(newItem, quantity, item):
    curObj.execute("UPDATE store SET item = ?, quantity = ? WHERE item = ? ",(newItem,quantity,item))
    connectDb.commit()

# create_table()
# insert_entry("black pepper",10,5)
# delete_entry("Face shiel")
update_entry("knorr pork cube",30,"black pepper")
print(view_entries())

connectDb.close()
