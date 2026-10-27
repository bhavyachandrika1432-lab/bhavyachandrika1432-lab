# Task 31
class Laptop:
    def __init__(self,brand,price,ram):
        self.brand=brand
        self.price=price
        self.ram=ram
    def display_details(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Ram:",self.ram)
Laptop1=Laptop("Samsung",50000,"8GB")
Laptop1.display_details()
#Task 32
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)
class ATM(Bank):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")
atm = ATM(5000)
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")