n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = {}
CD = {}

for a in A:
    for b in B: AB[a + b] = AB[a + b] + 1 if (a + b) in AB else 1

for c in C:
    for d in D: CD[c + d] = CD[c + d] + 1 if (c + d) in CD else 1

Result = 0
for key in AB.keys():
    if -key in CD: Result += AB[key] * CD[-key]

print(Result)