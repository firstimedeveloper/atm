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
		return (account)
	def check_pin(self, card_num, pin):
		for account in self.accounts:
			if card_num in account:
				if account.pin == pin:
					return True, account
		return False
	def get_balance(self, card_num, pin):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False, 0
		else:
			return True, account.cash
	def deposit(self, card_num, pin, cash):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False
		else:
			account.cash += cash
			return True
	def withdraw(self, card_num, pin, cash):
		err, account = self.check_pin(card_num, pin)
		if err == False:
			return False
		else:
			if (cash > account.cash):
				return False
			account.cash -= cash
			return True


class Atm:
	_authorized = False
	_card_num = 0
	_pin = 0
	def __init__(self, bank):
		self.bank = bank
	def insert_card(self, card_num, pin):
		if self.bank.check_pin(card_num, pin):
			print("Valid Card")
			self._authorized = True
			self._card_num = card_num
			self._pin = pin
			return True
		else:
			print("Invalid Card")
			self._authorized = False
			return False
	def see_balance(self):
		if self._authorized == False:
			print("Not Authorized")
			return False
		else:
			err, balance = self.bank.get_balance(self._card_num, self._pin)
			if err == False:
				print("Something went wrong...")
				return False
			else:
				print("Balance: $" + str(balance))
			return True
	def end(self):
		self._card_num = 0
		self._pin = 0
		self._authorized = False
	# testing ATM functionality
	def run(self):
		n = int(input("Enter the number of accounts to be created: "))
		for i in range(1, n+1):
			pin, cash = map(int, input("Account " + str(i) + ": Enter the pin number, and starting cash amount (pin, cash): ").split())
			account = self.bank.add_account(pin, cash)
			print(account)
		while (True):
			print("Starting the ATM simulation.")
			card_num = int(input("Please insert your card: "))
			pin = int(input("Please insert the pin number: "))
			err = self.insert_card(card_num, pin)
			break







"""
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
atm.insert_card(account.card_num, account.pin) """
bank = Bank()
atm = Atm(bank)
atm.run()
