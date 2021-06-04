class Account:
    def __init__ (self,name,phone,loan,loanLimit):
        self.phone = phone
        self.name = name
        self.balance = 0
        self.loan = loan
        self.loanLimit = 1000
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
    def borrow(self,loanLimit,amount):
