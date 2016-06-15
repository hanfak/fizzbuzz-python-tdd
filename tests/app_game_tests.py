import unittest
from app.game import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def test_1_return_number(self):
		self.assertEqual("1",self.fizzbuzz.count(1))

	def test_2_return_number_any(self):
		self.assertEqual("4",self.fizzbuzz.count(4))

	def test_3_return_fizz(self):
		self.assertEqual("Fizz", self.fizzbuzz.count(3))

	def test_4_return_fizz_any(self):
		self.assertEqual("Fizz", self.fizzbuzz.count(9))

	def test_5_return_buzz(self):
		self.assertEqual("Buzz", self.fizzbuzz.count(5))

	def test_6_return_buzz(self):
		self.assertEqual("Buzz", self.fizzbuzz.count(20))

	def test_7_return_fizzbuzz(self):
		self.assertEqual("FizzBuzz", self.fizzbuzz.count(15))

	def test_7_return_fizzbuzz(self):
		self.assertEqual("FizzBuzz", self.fizzbuzz.count(90))
