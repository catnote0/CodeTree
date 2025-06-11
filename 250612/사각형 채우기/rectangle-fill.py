n = int(input())

# Please write your code here.
fibonacci = [1, 1, 2]
for i in range(3, n + 1): fibonacci.append((fibonacci[-1] + fibonacci[-2]) % 10007)
print(fibonacci[n])