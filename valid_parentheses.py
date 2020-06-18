def check(a):
    stack = []
    pair = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
            }
    for i in a:
        if i in pair:
            stack.append(i)
        else:
            if not len(stack):
                return False
            last = stack.pop()
            if pair[last]!= pair:
                return False
    if len(stack):
        return False
    else:
        return True

n = input('enter the parenthese : ')
print(check(n))
