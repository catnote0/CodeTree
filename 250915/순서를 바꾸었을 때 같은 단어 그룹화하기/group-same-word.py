n = int(input())
words = [input() for _ in range(n)]

count = {}

for word in words:
    sortword = "".join(sorted(word))
    count[sortword] = count[sortword] + 1 if sortword in count else 1

print(max(count.values()))