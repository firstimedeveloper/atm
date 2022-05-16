import random
# no separate User class.
# instead, all Atm actions are per one account.
# a person can have multiple accounts.
class Account:
	def __init__(self, card_num, pin, initial_cash=0):
		self.card_num = card_num
		self.pin = pin
		self.cash = initial_cash
	def __contains__(self, card_num):
		return self.card_num == card_num
	def __str__(self):
		return "card no: " + str(self.card_num) + " pin: " + str(self.pin) + " cash: " + str(self.cash)



class Bank:
	def __init__(self):
		self.accounts = set()
		self.id_counter = 0
	def add_account(self, pin, initial_cash=0):
		account = Account(self.id_counter, pin, initial_cash)
		self.accounts.add(account)
		self.id_counter += 1
	def check_pin(self, card_num, pin):
		for account in self.accounts:
			if card_num in account:
				if account.pin == pin:
					return True, account
		return False
	def get_balance(self, card_num, pin):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False
		else:
			return account.cash
	def deposit(self, card_num, pin):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False
		else:
			return account.cash
	def withdraw(self, card_num, pin):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False
		else:
			return account.cash


class Atm:
	def __init__(self, bank):
		self.bank = bank
		self.account = None
		self.authorized = False
	def insert_card(self, card_num, pin):
		if self.bank.check_pin(card_num, pin):
			print("Valid Card")
			self.authorized = True
		else:
			print("Invalid Card")
			self.authorized = False
	def see_balance(self):
		if self.authorized == False:
			print("Not Authorized")
		else:
			print()

bank = Bank()
bank.add_account(1234, 0)
bank.add_account(12345, 0)
bank.add_account(12346, 0)
bank.add_account(12347, 0)
bank.add_account(12348, 0)

print(bank.accounts)
for account in bank.accounts:
	print(account)

account = Account(0, 1234)
atm = Atm(bank)
atm.insert_card(account.card_num, account.pin)
