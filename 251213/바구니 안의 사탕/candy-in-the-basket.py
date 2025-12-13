Max_Position = 1000000

n, k = map(int, input().split())
candy = []
pos = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

if k >= Max_Position:
    print(sum(candy))
    exit(0)

line = [0] * (Max_Position * 2 + 1)

for c, p in zip(candy, pos): line[p] += c

Sum = 0
for i in range(k * 2 + 1): Sum += line[i]

Result = Sum
for i in range(k * 2 + 1, Max_Position * 2 + 1):
    Sum += (line[i] - line[i - k * 2 - 1])
    Result = max(Result, Sum)

print(Result)