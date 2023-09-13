person1 = {
    'name': 'John', 
    'age': 25, 
    'city': 'New York'
    }
person2 = {
    'name': 'Jane', 
    'age': 30, 
    'city': 'London'
    }
person3 = {
    'name': 'Tom', 
    'age': 35, 
    'city': 'Paris'
    }

people_ = [person1,person2,person3]

for people in people_:
    print("name:",people['name'])
    print("age:",people['age'])
    print("city:",people['city'] + "\n")