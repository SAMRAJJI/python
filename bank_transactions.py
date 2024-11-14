class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def get_balance(self):
        return self.balance

def main():
    account = BankAccount("Alice")

    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current Balance: {account.get_balance()}")
        elif choice == '4':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid option. Please choose a valid option.")
        print(account)

if __name__=="__main__":
    main()




