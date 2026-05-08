class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("not money")
        else:
            self.balance -= amount
            
    def check_balance(self):
        print(self.balance)
        
acc = BankAccount(101,1000)

acc.deposit(1000)
acc.withdraw(100)
acc.check_balance()
            