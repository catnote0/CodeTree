N, M = map(int, input().split())

def select(now_max, cnt, result):
    if cnt == M:
        print(*result)
        return
    for i in range(now_max + 1, N + 1): select(i, cnt + 1, result + [i])

select(0, 0, [])