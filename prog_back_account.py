class BankAccount:
    def __init__(self,name,account_number,opening_balance=0):
        self.name=name
        self.account_number=account_number
        if opening_balance<0:
            print("invalid opening balance")
            self.balance=0
        else:
            self.balance=opening_balance
    def deposit(self,amount):
        if amount<0:
            print(f"deposit amount should be positive not {amount}")
        else:
            self.balance += amount
    def withdraw(self,amount):
        if amount<0:
            print("withdrw amount should be positive")
        elif amount>self.balance:
            print(f"insufficient balance:{self.balance},can't withdraw {amount}")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
    def __str__(self):
        return (f"Account[{self.account_number}-{self.name}:${self.balance}]")
a1=BankAccount("Alice","001",500)
a2=BankAccount("Bob","002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)
a2.deposit(-50)
a2.deposit(300)
print(a1)
print(a2)
