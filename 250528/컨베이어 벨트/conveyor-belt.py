n_conv = 2

n, t = map(int, input().split())
t %= (n * n_conv)
arr = []
for i in range(n_conv): arr += input().split()
arr = arr[(n * n_conv - t):(n * n_conv)] + arr[:(n * n_conv - t)]
for i in range(n_conv): print(*arr[(n * i) : (n * (i + 1))])