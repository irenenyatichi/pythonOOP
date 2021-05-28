class Bank:
    def __init__ (self,name,number,type):
        self.number = number
        self.name = name
        self.type = type
    def withdraw(self):
        return f"Bank Owner, {self.name} of account type {self.type}, wishes to withdraw {self.withdraw} from account number {self.number} "
    def deposit(self):
        return f"Bank Owner, {self.name} of account type {self.type}, wishes to deposit {self.deposit} from account number {self.number} "
