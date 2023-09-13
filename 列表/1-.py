names = ['cxk', 'lts', 'xl', 'any','rnm']

print(f"welcome\t{names[0]}")
print(f"welcome\t{names[1]}")
print(f"welcom\t{names[2]}")
print(f"welcome\t{names[3]}")
print(f"welcome\t{names[4]}")
    
print("sorry,rnm can't come.")

names.remove('rnm')
names.append('ctrl')

print(f"welcome\t{names[0]}")
print(f"welcome\t{names[1]}")
print(f"welcom\t{names[2]}")
print(f"welcome\t{names[3]}")
print(f"welcome\t{names[4]}")

print("i'm find a bigger table")

names.insert(0, 'a')
names.insert(3, 'b')
names.append('c')

print(f"welcome\t{names[0]}")
print(f"welcome\t{names[1]}")
print(f"welcom\t{names[2]}")
print(f"welcome\t{names[3]}")
print(f"welcome\t{names[4]}")
print(f"welcome\t{names[5]}")
print(f"welcome\t{names[6]}")
print(f"welcome\t{names[7]}")

print("oh,new table can't be delivered.\nonly two people can be invited.")

name = names.pop(2)
print(f"sorry,{name}")

name = names.pop(2)
print(f"sorry,{name}")

name = names.pop(2)
print(f"sorry,{name}")
name = names.pop(2)
print(f"sorry,{name}")

name = names.pop(2)
print(f"sorry,{name}")

name = names.pop(2)
print(f"sorry,{name}")

print(f"only {names[0]} and {names[1]}")

print(f"bye {names[0]}")
del names[0] 
print(f"bye {names[0]}")
del names[0]

print(names)



