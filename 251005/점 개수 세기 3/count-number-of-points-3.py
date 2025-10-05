n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

comp_list = set()
for p in points: comp_list.add(p)
comp_list = sorted(comp_list)

comp_dict = dict()
for i, n in enumerate(comp_list): comp_dict[n] = i

for a, b in queries: print(comp_dict[b] - comp_dict[a] + 1)