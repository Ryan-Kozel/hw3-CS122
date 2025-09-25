import shelve

from banking.accounts import SavingAccount, CheckingAccount


class Bank:
    def __init__(self, db_path):
        self.accounts = {}
        self.shelf = db_path

    def create_account(self, account_type, owner_name, initial_balance=0.0):
        """ 
        Create either a savings account or a checking account depending on account_type
        """
        #If account with owner's name already exists, print an error message and return False
        if owner_name in self.accounts:
            print(f"Account: {owner_name} already found")
            return False
        else:
        #If it does not exist, create it based on specified type
            if account_type.lower() == 'checking':
                acc = CheckingAccount(owner_name, initial_balance)
                self.accounts[acc.owner_name] = acc
                return True
            elif account_type.lower() == 'saving':
                acc = SavingAccount(owner_name, initial_balance)
                self.accounts[acc.owner_name] = acc
                return True

    def get_account(self, owner_name):
        """
        Find account stored in accounts dictionary, or return None if not found
        """
        if owner_name in self.accounts:
            return self.accounts[owner_name]
        else:
            return None

    def save_data(self):
        """
        Store the accounts dictionary in a shelve file
        """
        with shelve.open(self.shelf) as s:
            s['accounts'] = self.accounts

    def load_data(self):
        """
        Retrieve the accounts dictionary, returning an empty dictionary if the file does not exist
        """
        with shelve.open(self.shelf) as s:
            #Get the accounts dictionary, defaut value is an empty dictionary if not found
            self.accounts = s.get('accounts', {})
            return self.accounts

