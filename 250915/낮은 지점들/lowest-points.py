n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

pList = {}

for p in points:
    x, y = p
    pList[x] = min(pList[x], y) if x in pList else y

print(sum(pList.values()))
    