class FizzBuzz(object):
	def count(self, number):
		if self.__divisible_by(number, 15):
			return "FizzBuzz"

		if self.__divisible_by(number, 3):
			return "Fizz"

		if self.__divisible_by(number, 5):
			return "Buzz"

		return str(number)

	def __divisible_by(self, number, a):
		return number % a == 0
