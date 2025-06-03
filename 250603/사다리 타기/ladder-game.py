n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key = lambda x: x[1])
correct = [0]
result = m

def check(pos, edge_list):
    for edge in edge_list:
        if edge[0] == pos: pos += 1
        elif edge[0] == pos - 1: pos -= 1
    return pos

def select(num, count, edge_list):
    global result
    if num == m:
        for i in range(1, n + 1):
            if correct[i] != check(i, edge_list): return
        result = min(result, count)
        return
    select(num + 1, count, edge_list)
    select(num + 1, count + 1, edge_list + [edges[num]])

for i in range(1, n + 1): correct.append(check(i, edges))
select(0, 0, [])
print(result)