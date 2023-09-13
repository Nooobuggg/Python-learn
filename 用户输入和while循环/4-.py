sandwiches =  ["Italian Grilled Chicken Sandwich", "Ham and Cheese Sandwich", "Mexican Beef Sandwich"]
f_sandwiches = []
while sandwiches:
    f = sandwiches.pop()
    print(f"I made your {f}")
    f_sandwiches.append(f)
print(f"f_sandwiches: {f_sandwiches}")