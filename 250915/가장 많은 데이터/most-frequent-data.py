n = int(input())
words = [input() for _ in range(n)]

wordList = {}
for word in words: wordList[word] = wordList[word] + 1 if word in wordList else 1
print(max(wordList.values()))