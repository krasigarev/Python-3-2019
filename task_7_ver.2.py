# task_7  na drug

def compare(a, b) :
    if a is None and b is None :
        return a
    if a is None :
        return b
    if b is None :
        return b
    if a == b :
        return a
    if a > b :
        return a
    return b


kind = input().lower()
a = input()
b = input()

if kind == 'int' :
    print(compare(int(a), int(b)))
elif kind == 'char' :
    print(chr(compare(ord(a), ord(b))))
    # print(compare(str(a), str(b)))
elif kind == 'string' :
    print(compare(str(a), str(b)))
