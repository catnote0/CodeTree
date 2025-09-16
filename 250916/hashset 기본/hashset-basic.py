n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

S = set()

for c, v in zip(commands, x):
    if c == "add": S.add(v)
    elif c == "remove": S.remove(v)
    else: print("true" if v in S else "false")