K, N = map(int, input().split())

def select(num, List):
    if num > N:
        print(*List)
        return
    for i in range(1, K + 1): select(num + 1, List + [i])

select(1, [])


