import shelve

from banking.accounts import SavingAccount, CheckingAccount


class Bank:
    def __init__(self, db_path):
        self.accounts = {}
        self.shelf = db_path

    # TODO
    def create_account(self, account_type, owner_name, initial_balance=0.0):
        if owner_name in self.accounts:
            print(f"Account: {owner_name} already found")
            return False
        else:
            if account_type.lower() == 'checking':
                acc = CheckingAccount(owner_name, initial_balance)
                self.accounts[acc.owner_name] = acc
                return True
            elif account_type.lower() == 'saving':
                acc = SavingAccount(owner_name, initial_balance)
                self.accounts[acc.owner_name] = acc
                return True

    def get_account(self, owner_name):
        if owner_name in self.accounts:
            return self.accounts[owner_name]
        else:
            return None

    def save_data(self):
        with shelve.open(self.shelf) as s:
            s['accounts'] = self.accounts

    def load_data(self):
        with shelve.open(self.shelf) as s:
            self.accounts = s.get('accounts', {})
            return self.accounts

