n = "Where would you go? "
a = True
while a:
    message = input(n)
    if message != "quit":
        print(f"You would to go {message}")
    else:
        print("Thank you")
        a = False
