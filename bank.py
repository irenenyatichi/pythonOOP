class Account:
    def __init__ (self,name,phone):
        self.phone = phone
        self.name = name
        self.balance = 0
    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            return f"Dear {self.name} you have deposited {amount}. Your balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount <=0:
            return f"The amount must be greater than zero"
        elif self.balance<amount:
            return f"The amount withdrawn must be less than {self.balance}"
        else: 
            self.balance-=amount
            return f"Your balance is {self.balance}"
#TERMINAL 
# from bank import Account
# >>> acc1=Account(name = "Irene", phone="071234567")
# >>> acc1.deposit(10000)
# 'Dear Irene you have deposited 10000. Your balance is 10000'
# >>> acc1.withdraw(20000)
# 'The amount withdrawn must be less than 10000'
# >>> acc1.withdraw(5000)
# 'Your balance is 5000'
# >>> 