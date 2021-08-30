'''
Update your existing User class to have an association with the BankAccount class. 
You should not have to change anything in the BankAccount class. The method signatures 
of the User class (the first line of the method with the def keyword) should also remain the same.

For example, our User class currently has a method like this:
'''


class BankAccount:
    bankName = "Cloud Credit Union"
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate=3, balance=0):
        self.int_rate = (int_rate)
        self.balance = balance
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate/100)
        return self

    @classmethod
    def display_info(cls):
        print("You are Banking with", cls.bankName)


'''
class User:

    # other methods
    def make_deposit(self, amount):
        # hmmm...the User class doesn't have an account_balance attribute anymore
        self.account.balance += amount

But our User class no longer has a self.account_balance attribute. 
Instead, we have replaced this with an instance of a BankAccount by the name of self.account. 
That means our make_deposit (and other methods referencing self.account_balance) 
need to be updated! That's the goal of this assignment.

Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:

class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        print(self.account.balance)		# or access its attributes
'''


class user:
    def __init__(self, name=None):
        self.name = name
        self.account = BankAccount
        self.saving = None

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print("User {}, Balance: ${}".format(self.name, self.account.balance))

    def openSavingAccount(self):
        self.saving = BankAccount

# requested bonus section
    def transfer_money(self, amount):
        if self.saving == None:
            print("You don't have a saving account")
        else:
            if amount > self.account.balance:
                self.make_withdrawal(amount)
                self.saving.deposit(amount)
            elif amount < 0 and abs(amount) > self.saving.balance:
                self.saving.withdraw(amount)
                self.make_deposit(amount)
            else:
                print("insufficient balance")
