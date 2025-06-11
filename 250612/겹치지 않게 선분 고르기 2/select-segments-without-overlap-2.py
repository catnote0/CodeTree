n = int(input())
line = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append((a, b))

line.sort(key = lambda x: x[1])

last = -1
cnt = 0
for l in line:
    if last < l[0]:
        last = l[1]
        cnt += 1

print(cnt)