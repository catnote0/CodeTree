n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

p_Set = set()
for p in points: p_Set.add(p)
for a, b in queries:
    p_Set.add(a)
    p_Set.add(b)
p_List = list(p_Set)
p_List.sort()
p_Dict = dict()
for i, p in enumerate(p_List): p_Dict[p] = i

new_points = []
new_queries = []
for p in points: new_points.append(p_Dict[p])
for a, b in queries: new_queries.append((p_Dict[a], p_Dict[b]))

Line = [0] * 310000
for p in new_points: Line[p] = 1
for i in range(1, 300000): Line[i] += Line[i - 1]
for a, b in new_queries:
    if a == 0: print(Line[b])
    else: print(Line[b] - Line[a - 1])