from math import factorial
n, r = map(int, input().split())
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print(combination(n, r))
