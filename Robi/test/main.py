from pet import Pet
from owner import Owner

pet1 = Pet("Tom", "Blue cat with a white belly")
pet2 = Pet("Buddy", "Golden retriever with a wagging tail")
pet3 = Pet("Bugs", "Fluffy gray and white rabbit")
pet4 = Pet("Felix", "Black and white mischievous cat")

owner1 = Owner("Hans", 24, True)
owner2 = Owner("John", 30, False)

owner1.petsOwned = [pet1, pet2, pet3]
owner2.petsOwned = [pet4]

owner2.goOut()

print(f"{owner1.name} is {owner1.age} years old and has a")
for pet in owner1.petsOwned:
    print(pet.desc)
print(f"{owner1.name} is {'outside' if owner1.isOut else 'inside'}.")



print(f"{owner2.name} is {owner2.age} years old and has the following pets:")
for pet in owner2.petsOwned:
    print(pet.desc)
print(f"{owner2.name} is {'outside' if owner2.isOut else 'inside'}.")


