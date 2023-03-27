import sys
N, S = map(int, sys.stdin.readline().split(' '))
answer = 0

for red in range(1, N+1):
    for blue in range(1, N+1):
        if red + blue <= S:
            answer += 1

print(answer)
