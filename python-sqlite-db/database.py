import sqlite3

db = "customer.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

def create_table():
    CREATE_CUSTOMERS_TABLE = """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            email TEXT
        )
        
    """
    cur.execute(CREATE_CUSTOMERS_TABLE)
    conn.commit()
    print("Create table successfully...")
    
def select_customers():
    SELECT_CUSTOMERS = """
        SELECT * FROM customers
    """
    customers = cur.fetchall()
    
    return customers

def add_customer(fname,lname,email):
    ADD_CUSTOMER = """
        INSERT INTO customers (firstname,lastname,email)
        VALUES (?,?,?)
    """
    cur.execute(ADD_CUSTOMER, (fname,lname,email))
    conn.commit()
    
def close_db():
    conn.close()