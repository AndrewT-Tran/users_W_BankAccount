from bankAccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
        self.account.balance += amount
        print(self.account.balance)
        return self

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

    def display_account_balance(self):
        print("User: " + self.name, "|| Balance: " + str(self.account.balance))
        return self

    def transfer_money(self, amount, other_user):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


Andrew_Tran = User("Andrew Tran", "A.Tran@me.com")

Andrew_Tran.make_deposit(4000).make_withdraw(200).display_account_balance()
