fls = {
    'a':'1',
    'b':'2',
    'c':'3',
}
pfls = ['a','b','c','d']

for pfl in pfls:
    if pfl in fls.keys():
        print("Thank you ",pfl)
    else:
        print("Welcome ",pfl)