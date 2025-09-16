n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

S = set(arr1)

for num in arr2: print(1 if num in S else 0, end = " ")