from banking.exceptions import InvalidAmountError, InsufficientFundsError


class BankAccount:
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner_name = owner_name
        self.initial_balance = initial_balance
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit an amount into an account"""
        if amount <= 0: # make sure inputed amount is positive
            raise InvalidAmountError("Deposit must be positive", 200)
        else:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        raise NotImplementedError

    def __str__(self):
        string = "Account Owner: {name}, Balance: ${bal:.2f}".format(name=self.owner_name, bal=self.balance) #format to nice output message
        return string


class SavingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)

    def withdraw(self, amount):
        """ 
        Withdraw an amount from a savings account
        Savings accounts have withdraw fee of $2.00
        """
        
        fee = 2.00
        if amount < 0:  # make sure that withdraw amount is positive
            raise InvalidAmountError("Deposit must be positive", 200)
        elif amount + fee > self.balance:  # account cannot go into negatives
            raise InsufficientFundsError("Insufficient funds", 201)
        else:
            self.balance = self.initial_balance - amount - fee


class CheckingAccount(BankAccount):
    def __init__(self, owner_name, initial_balance=0.0):
        super().__init__(owner_name, initial_balance)

    def withdraw(self, amount):
        """ 
        Withdraw an amount from a checking account
        Savings accounts have withdraw fee of $1.00
        """
        fee = 1.00
        if amount < 0:  # make sure withdraw amount positive
            raise InvalidAmountError("Deposit must be positive", 200)
        elif amount + fee > self.balance:  # account cannot go into negatives
            raise InsufficientFundsError("Insufficient funds", 201)
        else:
            self.balance = self.balance - amount - fee
