def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance # Enables the re-binding of BALANCE in WITHDRAW
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance -= amount
        return balance
    return withdraw
