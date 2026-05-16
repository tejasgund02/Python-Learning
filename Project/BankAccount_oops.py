
class BankAccount:
    def __init__(self, account_number, initial_balance=0, account_holder=None):
        self.account_number = account_number
        self.balance = initial_balance
        self.account_holder = account_holder
        print(f"Account created for {self.account_holder} with account number {self.account_number} and initial balance {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}. New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        if amount > self.balance:
            print(f"Insufficient funds! in account {self.account_number}. Current Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New Balance: {self.balance}")
    
    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

# Example usage
ac1 = BankAccount("4343", 1000, "Tejas")
ac2 = BankAccount("4344")
# ac1.deposit(500)
# ac1.withdraw(200)   
# ac1.display_info()
ac2.deposit(300)
ac2.withdraw(100)
ac2.display_info()
