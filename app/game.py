class FizzBuzz(object):
	def count(self,number):
		if self.__divisible_by_15(number):
			return "FizzBuzz"

		if self.__divisible_by_3(number):
			return "Fizz"

		if self.__divisible_by_5(number):
			return "Buzz"

		return str(number)

	def __divisible_by_3(self,number):
		return number % 3 == 0

	def __divisible_by_5(self,number):
		return number % 5 == 0

	def __divisible_by_15(self,number):
		return number % 15 == 0
