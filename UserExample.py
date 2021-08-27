# Create a file with the User class, including the __init__ and make_deposit methods
class User:
   def __init__(self, name, email, account_balance):
      self.name = name
      self.email = email
      self.account_balance = account_balance

   def make_deposit(self, amount):
      self.account_balance += amount

# Add a make_withdrawal method to the User class
   def make_withdrawal(self, amount):
      self.account_balance -= amount

# Add a display_user_balance method to the User class
   def display_balance(self):
      print(f"User: {self.name}, Balance: {self.account_balance}")

# Transfer money method
   def transfer(self, amount, recipient):
      self.make_withdrawal(amount)
      recipient.make_deposit(amount)

# Create 3 instances of the User class   
Jaylen = User("Jaylen", "JBrown@Celtics.com", 4000000)
Marcus = User("Marcus", "MSmart@Celtics.com", 5000000)
Jayson = User("Jayson", "JTatum@Celtics.com", 6000000)

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
Jaylen.make_deposit(50)
Jaylen.make_deposit(500)
Jaylen.make_deposit(5000)
Jaylen.make_withdrawal(5000)
Jaylen.display_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
Marcus.make_deposit(50)
Marcus.make_deposit(500)
Marcus.make_withdrawal(5000)
Marcus.make_withdrawal(1000)
Marcus.display_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
Jayson.make_deposit(500)
Jayson.make_withdrawal(1000)
Jayson.make_withdrawal(5000)
Jayson.make_withdrawal(10000)
Jayson.display_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Jaylen.transfer(500, Jayson)
Jaylen.display_balance()
Jayson.display_balance()