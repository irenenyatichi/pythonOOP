class Account:
    def __init__ (self,name,phone):
        self.phone = phone
        self.name = name
        self.balance = 0
    # def withdraw(self):
    #     return f"{self.name} of {self.type} account, wishes to withdraw from account number {self.number} "
    def deposit(self,amount):
        self.balance+=amount
        return f"Dear {self.name} you have deposited {amount}. Your balance is {self.balance}"
    def show_balance(self):
        return self.balance