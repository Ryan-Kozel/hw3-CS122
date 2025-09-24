from banking.exceptions import InvalidAmountError, InsufficientFundsError


class BankAccount:
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit must be positive", 200)
        else:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        raise NotImplementedError

    def __str__(self):
        string = "Account Owner: {name}, Balance: ${bal:.2f}".format(name=self.owner_name, bal=self.balance)
        return string


class SavingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)

    def withdraw(self, amount):
        fee = 2.00
        if amount < 0:
            raise InvalidAmountError("Deposit must be positive", 200)
        elif amount + fee > self.balance:
            raise InsufficientFundsError("Insufficient funds", 201)
        else:
            self.balance = self.initial_balance - amount - fee


class CheckingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)

    def withdraw(self, amount):
        fee = 1.00
        if amount < 0:
            raise InvalidAmountError("Deposit must be positive", 200)
        elif amount + fee > self.balance:
            raise InsufficientFundsError("Insufficient funds", 201)
        else:
            self.balance = self.balance - amount - fee
