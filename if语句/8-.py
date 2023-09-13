names = ['b','admin','c','d','e']

if names:
    for name in names:
         if name == 'admin':
            print("Hello admin, would you like to see a status report?")
    
         else:
            print(f"Hello {name}")
else:
    print("We need to find some users!")