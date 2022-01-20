import psycopg2

connectDb = psycopg2.connect("dbname='store_db' user='postgres' password='DBadmin1122' host='localhost' port='5432'") # connect to database
curObj = connectDb.cursor() # make database connection object

# creating table
def create_table():
    curObj.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connectDb.commit()

# inserting data in table
def insert_entry(item, quantity, price):
    curObj.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    connectDb.commit()
    print("add entry")

# view entries in the database table
def view_entries():
    curObj.execute("SELECT * FROM store")
    entry = curObj.fetchall()
    
    return entry

# delete specific row
def delete_entry(item):
    curObj.execute("DELETE FROM store WHERE item = %s",(item,))
    connectDb.commit()
    print("delete row")

# update specific row
def update_entry(newItem, quantity, item):
    curObj.execute("UPDATE store SET item = %s, quantity = %s WHERE item = %s ",(newItem,quantity,item))
    connectDb.commit()
    print("update entry")

# create_table()
# insert_entry("Lucky me pancit canton original",5,15)
# delete_entry("Lucky me beef")
update_entry("lucky me chicken",12,"Lucky me pancit canton chilimansi")
print(view_entries())

connectDb.close()
