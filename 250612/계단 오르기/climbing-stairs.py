n = int(input())

a = [1, 0, 1, 1]

for i in range(4, n + 1): a.append((a[-2] + a[-3]) % 10007)
print(a[n])