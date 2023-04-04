N = int(input())
A = list(map(int, input().split(' ')))

answer = 0
answer += A.count(100) * A.count(400)
answer += A.count(200) * A.count(300)

print(answer)
