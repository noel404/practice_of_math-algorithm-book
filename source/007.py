import sys
N, X, Y = map(int, sys.stdin.readline().split(' '))
answer = 0

for i in range(1, N+1):
    if (i % X) == 0 or (i % Y) == 0:
        answer += 1
    else:
        pass

print(answer)
