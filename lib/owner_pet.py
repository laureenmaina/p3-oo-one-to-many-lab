class Pet:
    all=[] 
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of Owner class")
           

class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self): 
        return [pet for pet in Pet.all if pet.owner ==self]
    
    def add_pet(self,pet):
        if isinstance(pet,Pet):
                   TypeError("Owner object has no attribute pet_type")
        pet.owner = self

    def get_sorted_pets(self): 
        pets_list = self.pets()
        pets_list.sort(key=lambda pet: pet.name)
        return pets_list

        