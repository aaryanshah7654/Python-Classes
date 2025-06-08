# Practice problem
class stack:
    def __init__(self):
        self.element_list = []

    def push(self, item):
        self.element_list.append(item)

    def pop(self):
        if self.element_list:
            return self.element_list.pop()
        return "stack is empty"
    
    def peek(self):
        if self.element_list:
            return self.element_list[-1]
        return "stack is empty"
    
    def length(self):
        return len(self.element_list)
    
my_stack = stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print("Top item:", my_stack.peek())    
print("Stack size:", my_stack.length()) 

print("Popped:", my_stack.pop())         
print("Top item after pop:", my_stack.peek())  
print("Stack size after pop:", my_stack.length())  

class BankAccount:
    def __init__(self, name, account_number, amount=0):
        self.name = name
        self.account_number = account_number
        self.amount = amount
    
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.amount += deposit_amount
            print(f"Deposited ₹{deposit_amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print(f"Withdraw ₹{withdraw_amount}")
        else:
            print("Insufficient balance.")
    
    def check_balance(self):
        print(f"Account Balance: ₹{self.amount}")

account1 = BankAccount("Ram", "1234567890", 1000)
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()   
account1.withdraw(2000) 