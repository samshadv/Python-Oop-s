class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.__balance = balance
        
    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self,amount):
        if amount>self.__balance:
            print("not money")
        else:
            self.__balance -= amount
            
    def check_balance(self):
        print(self.__balance)
        
acc = BankAccount(101,1000)

acc.deposit(1000)
acc.withdraw(100)
acc.check_balance()
            