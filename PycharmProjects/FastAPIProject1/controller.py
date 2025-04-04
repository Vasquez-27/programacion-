from model import Pet
from view import pet_response, pet_list_response

class ABB:
    def __init__(self):
        self.pets = []

    def add(self, pet_id: int, name: str, breed: str):
        if any(p.pet_id == pet_id for p in self.pets):
            return False
        self.pets.append(Pet(pet_id, name, breed))
        return True

    def list(self):
        return [{"pet_id": p.pet_id, "name": p.name, "breed": p.breed} for p in self.pets]

abb = ABB()

def add_pet(pet_id: int, name: str, breed: str):
    if not abb.add(pet_id, name, breed):
        return pet_response("ID already exists")
    return pet_response("Pet added successfully")

def list_pets():
    return pet_list_response(abb.list())