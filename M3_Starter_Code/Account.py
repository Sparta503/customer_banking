class Account:
    """Creating an Account class with methods to manage balance and interest."""

    def __init__(self, balance=0.0, interest=0.0):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.interest
