N = int(input())
A = list(map(int, input().split(' ')))

def gcd(A, B):
    if A < B:
        A, B = B, A
    
    while A != 0 and B != 0:
        A = A % B
        A, B = B, A
    
    if A == 0:
        return B
    else:
        return A

cache = A[0]
for i in range(1, N):
    cache = gcd(cache, A[i])

print(cache)
