n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

wordList = {}

for i in range(1, len(words)): wordList[words[i]] = i

for q in queries: print(wordList[q] if q in wordList else words[int(q)])
    