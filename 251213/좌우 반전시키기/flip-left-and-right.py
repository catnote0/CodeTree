n = int(input())
arr = list(map(int, input().split()))

def Flip(pos): arr[pos] = 1 - arr[pos]

Count = 0
for i in range(1, n):
    if arr[i - 1] == 0:
        Count += 1
        Flip(i - 1)
        Flip(i)
        if i < n - 1: Flip(i + 1)

if arr[n - 1] == 0: print(-1)
else: print(Count)