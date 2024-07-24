class Account:
    # """An account has a balance and a holder.

    # >>> a = Account('John')
    # >>> a.holder
    # 'John'
    # >>> a.deposit(100)
    # 100
    # >>> a.withdraw(90)
    # 10
    # >>> a.withdraw(90)
    # 'Insufficient funds'
    # >>> a.balance
    # 10
    # >>> a.interest
    # 0.02
    # >>> Account.interest = 0.04
    # >>> a.interest
    # 0.04
    # """
    interest = 0.02 # A class attribute

    def __init__(self, account_holder): 
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        """Add AMOUNT to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract AMOUNT from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + withdraw_fee)

class Bank: 
    """A bank *has* accounts

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) >= 2