def main():
	print "lol"

def basicAritmeticSum(n):
    if n == 0:
        return 0
    else:
        return n + basicAritmeticSum(n - 1)

number = 10
print "The sum of the numbers 1 to " + str(number) + " is: " + str(basicAritmeticSum(number))