n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
check_list = []

last = 0x7FFFFFFF
for i in range(n):
    if last > cost[i]:
        check_list.append(i)
        last = cost[i]
check_list.append(n - 1)

Result = 0
for i in range(len(check_list) - 1): Result += sum(dist[check_list[i]:check_list[i + 1]]) * cost[check_list[i]]

print(Result)