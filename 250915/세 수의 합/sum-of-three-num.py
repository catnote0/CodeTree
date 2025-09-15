n, k = map(int, input().split())
arr = list(map(int, input().split()))

sumList = {}
Result = 0

for i in range(n):
    if (k - arr[i]) in sumList: Result += sumList[k - arr[i]]
    for j in range(i): sumList[arr[i] + arr[j]] = sumList[arr[i] + arr[j]] + 1 if (arr[i] + arr[j]) in sumList else 1

print(Result)