class Bank:
    def __init__ (self,name,number,type):
        self.number = number
        self.name = name
        self.type = type
    def withdraw(self):
        return f"{self.name} of {self.type} account, wishes to withdraw from account number {self.number} "
    def deposit(self):
        return f"{self.name} of {self.type} account, wishes to deposit from account number {self.number} "