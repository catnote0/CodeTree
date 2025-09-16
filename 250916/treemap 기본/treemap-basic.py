from sortedcontainers import SortedDict

n = int(input())
SDict = SortedDict()

for _ in range(n):
    line = input().split()
    cmd = line[0]
    if cmd == "add":
        k, v = int(line[1]), int(line[2])
        SDict[k] = v
    elif cmd == "remove":
        k = int(line[1])
        if k in SDict: del SDict[k]
    elif cmd == "find":
        k = int(line[1])
        print(SDict[k] if k in SDict else "None")
    else:
        if not SDict:
            print("None")
            continue
        for key, value in SDict.items(): print(value, end = " ")
        print()