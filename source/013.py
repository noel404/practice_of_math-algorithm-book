from math import sqrt, floor
N = int(input())
cache = 0

for i in range(1, floor(sqrt(N))+1):
    if cache == i :
        break
    if N % i == 0:
        cache = N//i
        print(i)
        print(N//i)
