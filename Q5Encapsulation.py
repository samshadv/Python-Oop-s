# Create a class BankAccount with private balance and methods to deposit and check balance

class BanckAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,amount):
        self.amount = amount 
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Amount can't be negative")
            
    def check_balance(self):
        return self.__balance
    
acc = BanckAccount(0)

acc.deposit(5000)
print("Balance", acc.check_balance())

acc.deposit(2000)
print("Balance", acc.check_balance())
