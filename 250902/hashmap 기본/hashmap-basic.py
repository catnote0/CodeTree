n = int(input())
myDict = {}
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        myDict[k] = v
    elif cmd == "remove":
        myDict.pop(k)
    else:
        if k in myDict: print(myDict[k])
        else: print("None")


# Please write your code here.
