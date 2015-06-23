import sys

# prints the sum of all even fibonacci numbers
# up to the number n
def theSumOfAllEvenFibonacciNumbers(n):
	sum = 0
	fibNumbers = [0, 1]
	turn = 0
	# loops until it breaks due to newNumber being 
	# bigger than the number n
	while True:
		newNumber = fibNumbers[0] + fibNumbers[1]
		if newNumber > n:
			break

		if newNumber % 2 == 0:
			sum += newNumber

		fibNumbers[turn] = newNumber

		# the turn-variable switches between 0 and 1 to
		# always update the smallest number in the array
		turn = (turn + 1) % 2

	print sum

# if the input from the terminal is two tokens
# then use that input, if the input is only one 
# token, use standard. If more than two, throw
# exception
if len(sys.argv) == 2:
	try:
		theSumOfAllEvenFibonacciNumbers((int)(sys.argv[1]))
	except ValueError:
		print "That input is not valid, please type a number!"
elif len(sys.argv) == 1:
	#the standard input
	theSumOfAllEvenFibonacciNumbers(4000000)
else:
	# this is used instead of throwing an exception, 
	# the program won't continue anyway
	print "ValueError: That input is too long! Try with just one additional number!"
