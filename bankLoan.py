from datetime import datetime

class Account:
    def __init__ (self,name,phone,transactions):
        self.phone = phone
        self.name = name
        self.balance = 0
        self.loan = 0
        self.loanLimit = 1000
        self.transactions = []
        self.withdrawals = []


    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            transaction = {"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
            # return f"Dear {self.name} you made the following transaction{self.transactions}"

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
        for withdrawal in self.withdrawals:
            narration = withdrawal["narration"]
            amount =withdrawal["amount"]
            balance = withdrawal["balance"]
            time = withdrawal["time"]
            print(f"Dear {self.name},a {narration} of {amount} on {time} was made. Your balance is {balance}.")
        for loans in self.loans:
            narration = loans["narration"]
            amount =loans["amount"]
            balance = loans["balance"]
            time = loans["time"]
            print(f"Dear {self.name}, a {narration} of {amount} on {time} was made. Your balance is {balance}.")
        for loanpay in self.loanpays:
            narration = loanpay["narration"]
            amount =loanpay["amount"]
            balance = loanpay["balance"]
            time = loanpay["time"]
            print(f"Dear {self.name}, a {narration} of {amount} on {time} was made. Your balance is {balance}.")