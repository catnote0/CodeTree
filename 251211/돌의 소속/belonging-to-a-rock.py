N, Q = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

Pref_Group = [[0] * 4 for _ in range(N + 1)]

for i in range(1, N + 1):
    Pref_Group[i] = Pref_Group[i - 1][:]
    Pref_Group[i][arr[i]] = Pref_Group[i - 1][arr[i]] + 1

for a, b in queries:
    for i in range(1, 4): print(Pref_Group[b][i] - Pref_Group[a - 1][i], end = " ")
    print()