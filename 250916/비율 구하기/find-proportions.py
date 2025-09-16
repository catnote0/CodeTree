from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]

SDict = SortedDict()

for word in words: SDict[word] = SDict[word] + 1 if word in SDict else 1

for key, value in SDict.items(): print("%s %.4f" % (key, (value / n * 100)))