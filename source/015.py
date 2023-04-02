A, B = map(int, input().split(' '))

if A < B:
    A, B = B, A

while (A != 0 and B != 0):
    A = A % B
    A, B = B, A

if A == 0:
    print(B)
else:
    print(A)
