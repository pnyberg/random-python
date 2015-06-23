#!/usr/bin/python
import sys

# prints the sum of all the numbers dividable
# by three or five up to the number n
def theSumOfAllNumbersDividableByThreeOrFive(n):
	sum = 0
	for i in range (0, n):
		# if the number i is dividable by three or five
		# add it to the sum
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	print sum

# if the input from the terminal is two tokens
# then use that input, if the input is only one 
# token, use standard. If more than two, throw
# exception
if len(sys.argv) == 2:
	try:
		theSumOfAllNumbersDividableByThreeOrFive((int)(sys.argv[1]))
	except ValueError:
		print "That input is not valid, please type a number!"
elif len(sys.argv) == 1:
	#the standard input
	theSumOfAllNumbersDividableByThreeOrFive(1000)
else:
	# this is used instead of throwing an exception, 
	# the program won't continue anyway
	print "ValueError: That input is too long! Try with just one additional number!"