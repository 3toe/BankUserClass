class BankAccount:
   def __init__(self, int_rate = 0.01, balance = 0):
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

A = BankAccount()
B = BankAccount(0.05, 3000000)

A.deposit(500).deposit(550).deposit(450).withdraw(800).yield_interest().display_account_info()
B.deposit(5000).deposit(5500).withdraw(4000).withdraw(8000).withdraw(80000).withdraw(100000).yield_interest().display_account_info()