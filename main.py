from math import factorial
def binom(n, k):
	return factorial(n)//(factorial(k)*factorial(n-k))
n,k = map(int, input().split())
print(binom(n,k))