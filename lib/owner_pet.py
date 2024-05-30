class Pet:
    all=[] #class variable all

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        #Define a class variable PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] and validate that the pet_type is one of those types in the __init__ method.
#raise Exception if this check fails.
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of Owner class")
           

class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self): #returns a full list of the owner's pet
        return [pet for pet in Pet.all if pet.owner ==self]
    
    def add_pet(self,pet): #checks that the the pet is of type Pet and adds the owner to the pet.
        if isinstance(pet,Pet):
                   TypeError("Owner object has no attribute pet_type")
        pet.owner = self

    def get_sorted_pets(self): # returns a sorted list of pets by their names.
        pets_list = self.pets()
        pets_list.sort(key=lambda pet: pet.name)
        return pets_list

        