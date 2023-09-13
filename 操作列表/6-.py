pizzas = ["cxkpizza","rnmpizza","ctrlpizza"]
friend_pizzas = pizzas[:]

pizzas.append("hhhpizza")
friend_pizzas.append("zypizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)