##############################################
# A set of rudimentary combinatorics functions
##############################################

def factorial (n):
	if n < 0 or not isinstance(n, int):
		return -1
	if n == 0 or n == 1:
		return 1
	else:
		result = 1
		for i in range(2, n + 1):
			result *= i
		return result


def permutations (n, r):
	if (
	        n < 0 or 
	        r < 0 or 
	        not isinstance(n, int) or not isinstance(r, int) or 
	        r > n
	    ):
		return -1
	if n == 0 or n == 1 or r == 0:
		return 1	
	else: 
		return factorial(n) / factorial(n - r)


def combinations (n, r):
	if (
	        n < 0 or 
	        r < 0 or 
	        not isinstance(n, int) or not isinstance(r, int) or 
	        r > n
	    ):
		return -1
	if n == 0 or n == 1 or r == 0:
		return 1	
	else: 
	    return permutations(n, r) / factorial(r)
