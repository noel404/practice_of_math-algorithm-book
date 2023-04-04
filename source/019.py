N = int(input())
A = list(map(int, input().split(' ')))

answer = 0
for i in [1, 2, 3]:
    if A.count(i) < 2:
        continue
    answer += int(A.count(i)*(A.count(i)-1)/2)
    
print(answer)
