'''create a  bank acount with members account number name type of account and balance.write constructor and method to deposit at the bank and withdraw an amount from the bank using simple code'''
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance!")
    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance: Rs.", self.balance)
acc_no = int(input("Enter Account Number: "))
name = input("Enter Name: ")
acc_type = input("Enter Account Type: ")
balance = float(input("Enter Balance: "))
b1 = BankAccount(acc_no, name, acc_type, balance)
print("\nInitial Account Details:")
b1.display()
amount = float(input("\nEnter Deposit Amount: "))
b1.deposit(amount)
amount = float(input("\nEnter Withdrawal Amount: "))
b1.withdraw(amount)
print("\nFinal Account Details:")
b1.display()

