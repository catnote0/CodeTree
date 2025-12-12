n = int(input())
a = [0] + list(map(int, input().split()))

Max = [-0x7FFFFFFF] * (n + 1)

for i in range(1, n + 1): Max[i] = max(Max[i - 1] + a[i], a[i])

print(max(Max))