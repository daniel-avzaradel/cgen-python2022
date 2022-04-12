class BankAccount:
    def __init__(self, id, balance, ownerId):
        self.id = id
        self.balance = balance
        self.ownerId = ownerId

    def deposit(self, value):
        self.balance += value
        return self.balance

    def withdraw(self, value):
        if self.balance < value:
            return self.balance
        else:
            self.balance -= value
            return self.balance
        
    
bankacc = BankAccount(1, 1000, 1)

print(bankacc.deposit(1000))
print(bankacc.withdraw(800))
print(bankacc.deposit(300))
print(bankacc.withdraw(100))
print(bankacc.balance)