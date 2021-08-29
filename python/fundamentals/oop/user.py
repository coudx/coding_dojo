'''
If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

For this assignment, we'll add some functionality to the User class:

make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
'''


class user:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print("User {}, Balance: ${}".format(self.name, self.balance))

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


a = user('a')
b = user('b')
c = user('c')

a.make_deposit(100)
a.make_deposit(200)
a.make_deposit(10000)
a.make_withdrawal(500)
a.display_user_balance()

b.make_deposit(5000)
b.make_deposit(500000)
b.make_withdrawal(200)
b.make_withdrawal(120)
b.display_user_balance()

c.make_deposit(500000)
c.make_withdrawal(1000)
c.make_withdrawal(2000)
c.make_withdrawal(1200)
c.display_user_balance()

a.transfer_money(c, 500)
a.display_user_balance()
c.display_user_balance()
