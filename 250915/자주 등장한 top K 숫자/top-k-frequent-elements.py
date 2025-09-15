n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}
for num in arr: count[num] = count[num] + 1 if num in count else 1

countList = []
for key, value in count.items(): countList.append([value, key])

countList.sort(reverse = True)

for i in range(k): print(countList[i][1], end = " ")