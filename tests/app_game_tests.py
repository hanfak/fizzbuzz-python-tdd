import unittest
from app.game import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def return_number_test_one(self):
		self.assertEqual("1",self.fizzbuzz.count(1))

	def return_number_test_two(self):
		self.assertEqual("4",self.fizzbuzz.count(4))
