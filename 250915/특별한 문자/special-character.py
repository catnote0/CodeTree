str = input()

count = {}

for c in str: count[c] = count[c] + 1 if c in count else 1

for c in str:
    if c not in count: continue
    if count[c] == 1:
        print(c)
        exit(0)

print("None")