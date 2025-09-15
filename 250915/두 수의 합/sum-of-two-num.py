n, k = map(int, input().split())
arr = list(map(int, input().split()))

nList = {}
Sum = 0

for num in arr:
    if (k - num) in nList: Sum += nList[k - num]
    nList[num] = nList[num] + 1 if num in nList else 1

print(Sum)