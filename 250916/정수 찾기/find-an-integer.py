n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

S = set(a)

for num in b: print(1 if num in S else 0)