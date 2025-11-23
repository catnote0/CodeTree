from sortedcontainers import SortedSet

n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

S = SortedSet()
for i in range(n): S.add((L[i], P[i]))

for cmd in commands:
    if cmd[0] == "rc":
        if cmd[1] == 1: print(S[-1][1])
        else: print(S[0][1])
    elif cmd[0] == "ad": S.add((cmd[2], cmd[1]))
    else: S.remove((cmd[2], cmd[1]))
    