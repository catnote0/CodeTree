from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key = cmp_to_key(lambda a, b: int(b + a) - int(a + b)))

print(''.join(arr))