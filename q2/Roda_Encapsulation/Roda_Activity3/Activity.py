
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = ""
        self.__balance = 0.0

        self.set_account_number(account_number)
        self.set_balance(balance)

    def set_account_number(self, new_number):
        if str(new_number).strip():
            self.__account_number = str(new_number)
        else:
            print("Warning: Invalid account number.")

    @property
    def account_number(self):
        return self.__account_number

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Warning: Balance cannot be negative.")

    @property
    def balance(self):
        return self.__balance


account = BankAccount("BA-2026-015", 12500.50)

print("BANK ACCOUNT DETAILS")
print("Account Number:", account.account_number)
print(f"Current Balance: ₱{account.balance:,.2f}")

account.set_account_number("BA-2026-028")
account.set_balance(18000.75)

print("\nUPDATED ACCOUNT DETAILS")
print("Account Number:", account.account_number)
print(f"Current Balance: ₱{account.balance:,.2f}")

account.set_balance(-500)

print(f"Final Balance: ₱{account.balance:,.2f}")
