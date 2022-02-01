class Account:
    
    def __init__(self,fp):
        self.filepath = fp
        with open(self.filepath, "r") as file:
            self.balance = float(file.read())
            
    def withdraw(self,amount):
        self.balance = self.balance - amount
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Checking(Account):
    
    """This class generates checking account objects"""
    
    type = "Checking account"
    def __init__(self, fp, fee):
        Account.__init__(self,fp)
        self.transFree = fee
        
    def transfer(self,amount):
        self.balance = self.balance - amount - self.transFree
            
account = Account("balance.txt")
checking = Checking("balance.txt",10)
romChecking = Checking("rom.txt",10)
mheannChecking = Checking("meann.txt",10)

print("Type:",romChecking.type)
print("Rom account balance:",romChecking.balance)
# romChecking.transfer(1000)
# romChecking.commit()
# print("Rom account balance:",romChecking.balance)

print("Type:",mheannChecking.type)
print("Mheann account balance:",mheannChecking.balance)
# mheannChecking.transfer(500)
# mheannChecking.commit()
# print("Mheann account balance:",mheannChecking.balance)

print(checking.__doc__)