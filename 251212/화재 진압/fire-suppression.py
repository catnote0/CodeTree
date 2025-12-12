n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

fires.sort()
stations.sort()

s = 0

Result = 0
for f in range(n):
    while s < m and stations[s] < fires[f]: s += 1
    if s == 0: Result = max(Result, abs(stations[s] - fires[f]))
    elif s == m: Result = max(Result, abs(stations[s - 1] - fires[f]))
    else: Result = max(Result, min(abs(stations[s - 1] - fires[f]), abs(stations[s] - fires[f])))

print(Result)