N = int(input())

fibonacci = [0, 1]
for i in range(2, N + 1): fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci[-1])