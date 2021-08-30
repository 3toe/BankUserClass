class BankAccount:
   def __init__(self, int_rate, balance):
      self.int_rate = int_rate
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      return self

   def withdraw(self, amount):
      if self.balance < amount:
         print("Insufficient funds for that withdrawal, and since we are a bank (aka exploitative debt slavers that exist to perpetuate class warfare by syphoning working class wages and assets to the elite while providing little to no societal value), we are charging you 5 dollars for not having enough dollars. Have a nice day")
         self.balance -= 5
      self.balance -= amount
      return self

   def display_account_info(self):
      print(f"Balance: ${self.balance}. Interest rate: {self.int_rate}")
      return self

   def yield_interest(self):
      if self.balance > 0 and self.int_rate > 0:
         self.balance += (self.int_rate * self.balance)
      return self

# End of BankAccount class

# Create a file with the User class, including the __init__ and make_deposit methods
class User:
   def __init__(self, name, email, account):
      self.name = name
      self.email = email
      self.account = BankAccount(int_rate=0.02, balance=0)

# Add a make_deposit method to the User class
   def make_deposit(self, amount):
      self.account.deposit(amount)
      return self

# Add a make_withdrawal method to the User class
   def make_withdrawal(self, amount):
      self.account.withdraw(amount)
      return self

# Add a display_user_balance method to the User class
   def display_balance(self):
      print(f"User: {self.name}, Balance: {self.account.balance}")
      return self

# test
A = User("me", "me@me.com", BankAccount)

A.make_deposit(100)
A.display_balance()
A.make_withdrawal(50)
A.display_balance()