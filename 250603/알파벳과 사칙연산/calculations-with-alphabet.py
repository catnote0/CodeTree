expression = input()
n = len(expression)
variable = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
Result = -0x7FFFFFFFF

def compute():
    value = variable[expression[0]]
    for i in range(1, n, 2):
        if expression[i] == '+': value = value + variable[expression[i + 1]]
        if expression[i] == '-': value = value - variable[expression[i + 1]]
        if expression[i] == '*': value = value * variable[expression[i + 1]]
    return value

def substitute(var):
    global Result
    if ord(var) > ord('f'):
        Result = max(Result, compute())
        return
    for i in range(1, 5):
        variable[var] = i
        substitute(chr(ord(var) + 1))

substitute('a')
print(Result)