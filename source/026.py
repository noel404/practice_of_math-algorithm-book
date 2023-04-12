N = int(input())

answer = 0
g = N
for i in range(1, N):
    answer += 1/(1-(i/N))

print(answer+1)
