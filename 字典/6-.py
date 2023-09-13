pet_owners1 = {'owner_name': 'Alice', 
           'pet_name': 'Buddy'
          }
pet_owners2 = {'owner_name': 'Bob', 
           'pet_name': 'Max'
          }
pet_owners3 = {'owner_name': 'Charlie', 
           'pet_name': 'Lucy'
          }

pet_owners = [pet_owners1,pet_owners2,pet_owners3]

for pet_owners in pet_owners:
    print("owner:",pet_owners['owner_name'])
    print("pet:",pet_owners['pet_name'] + "\n")

