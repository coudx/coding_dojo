class user:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print("User {}, Balance: ${}".format(self.name, self.balance))

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


a = user('a')
b = user('b')
c = user('c')

a.make_deposit(100).make_deposit(200).make_deposit(
    10000).make_withdrawal(500).display_user_balance()

b.make_deposit(5000).make_deposit(500000).make_withdrawal(
    200).make_withdrawal(120).display_user_balance()

c.make_deposit(500000).make_withdrawal(1000).make_withdrawal(
    2000).make_withdrawal(1200).display_user_balance()

a.transfer_money(c, 500)
a.display_user_balance()
c.display_user_balance()
