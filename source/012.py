import math
N = int(input())

answer = 'Yes'
for i in range(2, int(math.sqrt(math.floor(N)))):
    if N % i == 0:
        answer = 'No'
        break
    
print(answer)
