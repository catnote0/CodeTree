n = int(input())
x = []

for _ in range(n): x.append((tuple(map(int, input().split()))))

x.sort(key = lambda x: x[1])

right = -1
count = 0

for line in x:
    if right < line[0]:
        right = line[1]
        count += 1

print(count)