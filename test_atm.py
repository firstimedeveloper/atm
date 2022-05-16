import unittest
from atm import *

class TestBankMethods(unittest.TestCase):

	def test_check_pin(self):
		bank = Bank()
		f = open("test_input", "r")
		n = int(f.readline())
		for i in range(1, n+1):
			pin, cash = map(int, f.readline().split())
			account = bank.add_account(pin, cash)
		for i in range(1, n+1):
			test_card_num, test_pin = map(int, f.readline().split())
			self.assertTrue(bank.check_pin(test_card_num, test_pin))
		f.close()
	def test_deposit(self):
		bank = Bank()
		f = open("test_input", "r")
		n = int(f.readline())
		for i in range(1, n+1):
			pin, cash = map(int, f.readline().split())
			account = bank.add_account(pin, cash)
		test_card_num, test_pin = map(int, f.readline().split())
		bank.deposit(test_card_num, test_pin, 1000)
		_, temp = bank.balance(test_card_num, test_pin)
		self.assertEqual(temp, 1100)
		f.close()
	def test_withdraw(self):
		bank = Bank()
		f = open("test_input", "r")
		n = int(f.readline())
		for i in range(1, n+1):
			pin, cash = map(int, f.readline().split())
			account = bank.add_account(pin, cash)
		test_card_num, test_pin = map(int, f.readline().split())
		err = bank.withdraw(test_card_num, test_pin, 1000)
		self.assertFalse(err)
		bank.withdraw(test_card_num, test_pin, 10)
		_, val = bank.balance(test_card_num, test_pin)
		self.assertEqual(val, 90)
		f.close()


if __name__ == '__main__':
	unittest.main()
