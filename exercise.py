# Task: Task: In Python, demonstrate the concept of encapsulation using a class called BankAccount. This class should:Have private instance variables for account_number and balance. Include a constructor that initializes the account number and balance. Provide public methods to deposit and withdraw funds, ensuring no withdrawals exceed the available balance. Include a method to display the balance.

class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    
    def deposit(self, amount):
       

        if self.balance + amount < 0:
            return

        self.balance += amount
    
    def display_balance(self):
        print(self.balance)