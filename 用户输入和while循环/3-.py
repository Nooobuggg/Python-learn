age = "How old are u? "
i = True

while i:
    m = input(age)
    m = int(m)
    if m < 3:
        print("free")
    elif m >= 3 and m <= 12:
        print("10 dollars")
    else:
        print("15 dollars")