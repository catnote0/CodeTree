from sortedcontainers import SortedSet

n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)

S = SortedSet()

for cmd, n in zip(command, x):
    if cmd == "add": S.add(n)
    if cmd == "remove": S.remove(n)
    if cmd == "find": print("true" if n in S else "false")
    if cmd == "lower_bound": print(S[S.bisect_left(n)] if S.bisect_left(n) < len(S) else "None")
    if cmd == "upper_bound": print(S[S.bisect_right(n)] if S.bisect_right(n) < len(S) else "None")
    if cmd == "largest": print(S[-1] if S else "None")
    if cmd == "smallest": print(S[0] if S else "None")