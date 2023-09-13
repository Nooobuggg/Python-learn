p = "pizza ingredient:"
a = True

while a:
    m = input(p)
    if m != 'quit':
        print(m)
    elif m == 'quit':
        a = False