n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0

while a < len(A):
    if A[a] == B[b]: b += 1
    a += 1
    if b == len(B):
        print("Yes")
        exit(0)
print("No")