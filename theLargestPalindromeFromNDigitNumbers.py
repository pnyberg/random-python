import sys

# TODO: comment and effectivigize

def theLargestPalindromeFromTwoNDigitNumbers(n):
	product = 0
	firstNumber = pow(10, n)

	while True:
		secondNumber = firstNumber
		while secondNumber > 0:
			newProduct = firstNumber * secondNumber

			if isPalindrome(newProduct):
				product = max(product, newProduct)
			secondNumber -= 1
		firstNumber -= 1

	print product

def isPalindrome(palindrome):
	text = str(palindrome)
	start = 0
	end = len(text) - 1

	while start <= end:
		if text[start] != text[end]:
			return False

		start += 1
		end -= 1

	return True

# if the input from the terminal is two tokens
# then use that input, if the input is only one 
# token, use standard. If more than two, throw
# exception
if len(sys.argv) == 2:
	try:
		theLargestPalindromeFromTwoNDigitNumbers((int)(sys.argv[1]))
	except ValueError:
		print "That input is not valid, please type a number!"
elif len(sys.argv) == 1:
	#the standard input
	theLargestPalindromeFromTwoNDigitNumbers(3)
else:
	# this is used instead of throwing an exception, 
	# the program won't continue anyway
	print "ValueError: That input is too long! Try with just one additional number!"
