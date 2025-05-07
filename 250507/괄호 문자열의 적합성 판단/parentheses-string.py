str = input()

def Check():
    cnt = 0
    for a in str:
        if a == '(': cnt += 1
        if a == ')':
            cnt -= 1
            if cnt < 0:
                print("No")
                return
    if cnt != 0: print("No")
    else: print("Yes")

Check()