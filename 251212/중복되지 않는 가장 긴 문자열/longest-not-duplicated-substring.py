word = input()
n = len(word)

Dict = {word[0]: 1}
left = 0
right = 0
Result = 1

while right < n - 1:
    if word[right + 1] in Dict:
        Dict[word[left]] -= 1
        if Dict[word[left]] == 0: del Dict[word[left]]
        left += 1
    else:
        right += 1
        Dict[word[right]] = 1
        Result = max(Result, right - left + 1)

print(Result)