class BankAccount:
    def __init__(self, owner, amount):
        self.owner = owner
        self.__balance = amount  # Private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} deposited. New balance: {self.__balance}')
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient funds.')
        else:
            self.__balance -= amount
            print(f'{amount} withdrawn. New balance: {self.__balance}')
        
    def get_balance(self):
        return self.__balance

# Example usage
account_owner = BankAccount('Alice', 1000)
account_owner.__balance = 5000  # Attempt to directly modify the private attribute (will not work)
print(account_owner.get_balance())  # Output: 1000
account_owner.deposit(500)  # Output: 500 deposited. New balance: 1500
account_owner.withdraw(200)  # Output: 200 withdrawn. New balance: 1300
