n, t = map(int, input().split())
t %= (n * 3)
arr = []
for i in range(3): arr += input().split()
arr = arr[(n * 3 - t):(n * 3)] + arr[:(n * 3 - t)]
print(*arr[:n])
print(*arr[n:(n * 2)])
print(*arr[(n * 2):])