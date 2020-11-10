# coding: utf-8

class Bank_account:
    """
        Bank account class
    """

    def __init__(self, account_number, name, account_balance):
        """
            constructor
        """

        self.account_number = account_number
        self.name = name
        self.account_balance = account_balance

    def payment(self, amount):
        """
            add the amount to the account balance
        """
        self.account_balance += amount

    def withdrawal(self, amount):
        """
            remove the amount from the account balance
        """
        # check if enought on the account
        if amount >= self.account_balance:
            print("Solde insuffisant")
        else:
            self.account_balance -= amount

    def charges(self):
        """
            calculate the bank charges
        """
        self.account_balance = self.account_balance*95/100


if __name__ == "__main__":
    new_account = Bank_account(123456789, "Lola Lou", 666)
    print(f"\nLe numéro de compte est : {new_account.account_number}")
    print(f"Nom du propriétaire : {new_account.name}")
    print(f"Le solde du compte : {new_account.account_balance}\n")

    new_account.payment(1256)
    print("Versement de 1256..." )
    print(f"\nLe numéro de compte est : {new_account.account_number}")
    print(f"Nom du propriétaire : {new_account.name}")
    print(f"Le solde du compte : {new_account.account_balance}\n")

    
    print("Retrait souhaité de 3000..." )
    print(f"\nLe numéro de compte est : {new_account.account_number}")
    print(f"Nom du propriétaire : {new_account.name}")

    new_account.withdrawal(3000)

    print(f"\nLe solde du compte : {new_account.account_balance}\n")

    print("Retrait des agios sur le solde du compte")
    new_account.charges()
    print(f"Le solde du compte : {new_account.account_balance}\n")

