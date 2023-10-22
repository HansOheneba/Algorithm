from pet import Pet
from owner import Owner

pet1 = Pet("Tom", "Blue cat with a white belly")
pet2 = Pet("Buddy", "Golden retriever with a wagging tail")
pet3 = Pet("Bugs", "Fluffy gray and white rabbit")
pet4 = Pet("Felix", "Black and white mischievous cat")


owner1 = Owner("Hans", 30, True)
owner2 = Owner("John", 25, False)


owner1.petsOwned = [pet1, pet2, pet3]
owner2.petsOwned = [pet4]


owner2.goOut()

for pet in owner1.petsOwned:
    pet.intro()
print(f"{owner1.name} is {'outside' if owner1.isOut else 'inside'}.")


for pet in owner2.petsOwned:
    pet.intro()
print(f"{owner2.name} is {'outside' if owner2.isOut else 'inside'}.")

