from math import floor, sqrt

N = int(input())
answers = []

for i in range(2, floor(sqrt(N))):
    while N % i == 0:
        N = N // i
        answers.append(i)

if N >= 2:
    answers.append(N)

print(*answers)
