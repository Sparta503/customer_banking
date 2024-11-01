from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the balance."""
    savings_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return savings_account.get_balance(), savings_account.get_interest()

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the balance."""
    cd_account = Account(balance, 0)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    return cd_account.get_balance(), cd_account.get_interest()
