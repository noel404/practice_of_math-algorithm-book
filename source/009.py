import sys
N, S = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))

answer = 'No'
for i in range(1 << N):
    cache = 0
    for j in range(0, N):
        if (i & (1 << j)) != 0:
            cache += A[j]
    
    if cache == S:
        answer = 'Yes'
        break

print(answer)
