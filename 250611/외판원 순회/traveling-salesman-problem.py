n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

visited = [True] + [False] * (n - 1)
result = 0x7FFFFFFF

def visit(last, cnt, dist):
    global result
    if cnt == n:
        if not A[last][0]: return
        result = min(result, dist + A[last][0])
        return
    for i in range(n):
        if visited[i] or not A[last][i]: continue
        visited[i] = True
        visit(i, cnt + 1, dist + A[last][i])
        visited[i] = False

visit(0, 1, 0)
print(result)
