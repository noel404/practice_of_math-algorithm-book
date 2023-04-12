N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    answer += A[i] * (2/6) + B[i] * (4/6)

print(answer)
