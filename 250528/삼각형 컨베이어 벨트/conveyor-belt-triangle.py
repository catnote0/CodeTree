n, t = map(int, input().split())
t %= (n * 3)
arr = []
for i in range(3): arr += list(map(int, input().split()))
arr = arr[(n * 3 - t):(n * 3)] + arr[:(n * 3 - t)]
print(" ".join(map(str, arr[:n])))
print(" ".join(map(str, arr[n:(n * 2)])))
print(" ".join(map(str, arr[(n * 2):])))