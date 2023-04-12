N = int(input())
answer = 0
for i in range(N):
    p, q = map(int, input().split())
    answer += q * (1/p)

print(answer)
