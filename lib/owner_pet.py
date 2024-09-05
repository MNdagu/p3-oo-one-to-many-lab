class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f'{pet_type} not in PET TYPES. Allowed pet types are: {", ".join(Pet.PET_TYPES)}')
        self._pet_type = pet_type


class Owner:
    def __init__(self, name) -> None:
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} must be an instance of the Pet class")
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda pet : pet.name)

alice = Owner("Alice")
bob = Owner("Bob")

buddy = Pet(name="Buddy", pet_type="dog", owner=alice)
charlie = Pet(name="Charlie", pet_type="cat")
max = Pet(name="Max", pet_type="dog", owner=alice)

bob.add_pet(charlie)

print(alice.pets())  
print(bob.pets())    

print(alice.get_sorted_pets())  