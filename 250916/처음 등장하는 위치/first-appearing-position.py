from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))
SDict = SortedDict()

for i, num in enumerate(arr):
    if num not in SDict: SDict[num] = i + 1

for key, value in SDict.items(): print(key, value)