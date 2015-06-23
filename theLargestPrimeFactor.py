import sys, math

# prints the largest prime factor
def theLargestPrimeFactor(n):
	largestPrimeFactor = 1
	i = 2
	while i * i <= n:
		while n % i == 0:
			largestPrimeFactor = i
			n /= i
		i += 1

	print max(n, largestPrimeFactor)

# if the input from the terminal is two tokens
# then use that input, if the input is only one 
# token, use standard. If more than two, throw
# exception
if len(sys.argv) == 2:
	try:
		theLargestPrimeFactor((int)(sys.argv[1]))
	except ValueError:
		print "That input is not valid, please type a number!"
elif len(sys.argv) == 1:
	#the standard input
	theLargestPrimeFactor(600851475143)
else:
	# this is used instead of throwing an exception, 
	# the program won't continue anyway
	print "ValueError: That input is too long! Try with just one additional number!"
