n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

t %= (n * 2)
r1 = " ".join(map(str, d[(n - t % n):n] + u[:(n - t % n)]))
r2 = " ".join(map(str, u[(n - t % n):n] + d[:(n - t % n)]))
print(r1 + "\n" + r2 if t < n else r2 + "\n" + r1)