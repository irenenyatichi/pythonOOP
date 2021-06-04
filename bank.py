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
        elif balance<amount:
            return f"Dear {self.name} you have deposited {amount}. Your balance is {self.balance}"
        else: 
            self.balance-=amount
            return f"Your balance is {self.balance}"