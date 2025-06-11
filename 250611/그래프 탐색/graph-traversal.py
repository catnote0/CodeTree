n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[1] = True

def search(num):
    for next_vertex in adj_list[num]:
        if visited[next_vertex]: continue
        visited[next_vertex] = True
        search(next_vertex)

for x, y in edges:
    adj_list[x].append(y)
    adj_list[y].append(x)

search(1)
print(sum(1 if visit else 0 for visit in visited) - 1)