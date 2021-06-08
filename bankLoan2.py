from datetime import datetime, time

class Account:
    def __init__ (self,name,phone,transactions):
        self.phone = phone
        self.name = name
        self.balance = 0
        self.loan = 0
        self.loanLimit = 1000
        self.transactions = []

    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            transaction = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
            return f"Dear {self.name} you made the following transaction{self.transactions}"

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
    def borrow(self,amount):
        if amount<=self.loanLimit:
            self.loan+=amount
            self.balance+=self.loan
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan is KES{self.loan}, your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is KES{self.loan_limit}"
    
    def get_statement(self):
        for transaction in self.transactions:
            narration = transaction["narration"]
            amount = transaction["amount"]
            balance = transaction["balance"]
            time = transaction["time"]
            print(f"{time.strftime('%D')} {narration} an amount of {amount}. Your balance is {balance}")