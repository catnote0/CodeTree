n = int(input())
a = list(input())
b = list(input())

def Flip(start, end):
    for i in range(start, end + 1): a[i] = 'G' if a[i] == 'H' else 'H'

Count = 0
for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        Count += 1
        Flip(0, i)

print(Count)