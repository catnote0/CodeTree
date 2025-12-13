N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
score = [b[0] for b in bombs]
time_limit = [b[1] for b in bombs]

bombs.sort(key = lambda x: -x[0])

time_check = [0] * (max(time_limit) + 1)

for sc, tl in bombs:
    for i in range(tl, 0, -1):
        if time_check[i] == 0:
            time_check[i] = sc
            break

print(sum(time_check))