from bank_operations import create_savings_account, create_cd_account

def prompt_for_float(prompt, min_value=0):
    """Prompts the user for a floating-point input with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def prompt_for_int(prompt, min_value=0):
    """Prompts the user for an integer input with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def confirm_account_details(account_type, balance, interest_rate, months):
    """Displays account details and asks the user to confirm or re-enter information."""
    print(f"\nPlease confirm the {account_type} Account information:")
    print(f" - Balance: ${balance:.2f}")
    print(f" - Annual Interest Rate (APR): {interest_rate}%")
    print(f" - Duration: {months} months")
    
    confirmation = input("Is this information correct? (yes/no): ").strip().lower()
    return confirmation == 'yes'

def main():
    """Main function to handle savings and CD account setup, calculations, and display."""
    
    # Set up and validate Savings Account
    while True:
        print("\n--- Savings Account Setup ---")
        savings_balance = prompt_for_float("Enter the initial balance for the savings account: ")
        savings_interest = prompt_for_float("Enter the annual interest rate (APR) for the savings account (%): ")
        savings_maturity = prompt_for_int("Enter the number of months to calculate interest for the savings account: ")

        if confirm_account_details("Savings", savings_balance, savings_interest, savings_maturity):
            break
        print("Please re-enter the Savings Account information.\n")

    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )
    print(f"\nSavings Account - Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Savings Account - Updated Balance after {savings_maturity} months: ${updated_savings_balance:.2f}")

    # Set up and validate CD Account
    while True:
        print("\n--- CD Account Setup ---")
        cd_balance = prompt_for_float("Enter the initial balance for the CD account: ")
        cd_interest = prompt_for_float("Enter the annual interest rate (APR) for the CD account (%): ")
        cd_maturity = prompt_for_int("Enter the number of months to calculate interest for the CD account: ")

        if confirm_account_details("CD", cd_balance, cd_interest, cd_maturity):
            break
        print("Please re-enter the CD Account information.\n")

    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )
    print(f"\nCD Account - Interest Earned: ${cd_interest_earned:.2f}")
    print(f"CD Account - Updated Balance after {cd_maturity} months: ${updated_cd_balance:.2f}")

    print("\nThank you for using the Customer Banking System!")

if __name__ == "__main__":
    main()
