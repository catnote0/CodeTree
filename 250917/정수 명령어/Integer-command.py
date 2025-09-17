from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    SS = SortedSet()

    for cmd, num in zip(command, n):
        if cmd == "I": SS.add(num)
        elif SS:
            if num == 1: del SS[-1]
            else: del SS[0]
    
    if not SS: print("EMPTY")
    else: print(SS[-1], SS[0])