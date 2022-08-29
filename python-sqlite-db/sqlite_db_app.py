import database as db

db.create_table()

menu = """
Customers Record App

SELECT:
1. Add customer
2. Customers Records
3. Update Customer Record
4. Delete Customer Record
5. Exit
"""
print(menu)
selectOption = input("Choose 1-5 option: ")

while selectOption != "5":
    
    if selectOption == "1":
        firstName = input("Enter your firstname: ")
        lastName = input("Enter your lastname: ")
        email = input("Enter your Email:")
        
        db.add_customer(firstName,lastName,email)
        
    elif selectOption == "2":
        customers = db.select_customers()
        
        if len(customers) == 0:
            print("Customers Record Empty")
        else:
            for customer in customers:
                print(customer[0], customer[1], customer[2], customer[3])
    
    print(menu)
    selectOption

db.close_db()