from model.pet import Pet


class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if self.root is None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def delete(self, id: int):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        self.root = self.root.delete(id)

    def update(self, pet: Pet, id: int):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root.update(pet, id)

    def inorder(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.inorder()

    def preorder(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.preorder()

    def postorder(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.postorder()

    def count_by_breed(self):
        if not self.root:
            return {}
        return self.root.count_by_breed()

    def get_ids(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.list_ids()

    def report_by_location_and_gender(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.report_by_location_and_gender()

    def average_age_by_gender(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.average_age_by_gender()



class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet: Pet):
        if pet.id == self.pet.id:
            raise Exception("La mascota ya existe")
        if pet.id < self.pet.id:
            if self.left is not None:
                self.left.add(pet)
            else:
                self.left = NodeABB(pet)
        else:
            if self.right is not None:
                self.right.add(pet)
            else:
                self.right = NodeABB(pet)
        self.size += 1

    def delete(self, id: int):
        if id < self.pet.id:
            if self.left:
                self.left = self.left.delete(id)
        elif id > self.pet.id:
            if self.right:
                self.right = self.right.delete(id)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            # Buscar el menor de la rama derecha
            temp = self.right
            while temp.left:
                temp = temp.left
            self.pet = temp.pet
            self.right = self.right.delete(temp.pet.id)
        return self

    def update(self, pet: Pet, id: int):
        if self.pet.id == id:
            self.pet.name = pet.name
            self.pet.age = pet.age
            self.pet.breed = pet.breed
        elif id < self.pet.id:
            if self.left is not None:
                self.left.update(pet, id)
            else:
                raise Exception("Mascota con ese ID no encontrada")
        else:  # id > self.pet.id
            if self.right is not None:
                self.right.update(pet, id)
            else:
                raise Exception("Mascota con ese ID no encontrada")

    def average_age_by_gender(self):
        counts = {"Macho": 0, "Hembra": 0}
        total_age = {"Macho": 0, "Hembra": 0}

        def infer_gender(name):
            return "Hembra" if name[-1].lower() == "a" else "Macho"

        def traverse(node):
            if not node:
                return
            gender = infer_gender(node.pet.name)
            counts[gender] += 1
            total_age[gender] += node.pet.age
            traverse(node.left)
            traverse(node.right)

        traverse(self)

        return {
            "Macho": total_age["Macho"] / counts["Macho"] if counts["Macho"] else 0,
            "Hembra": total_age["Hembra"] / counts["Hembra"] if counts["Hembra"] else 0
        }


    def inorder(self):
        pets = []
        if self.left is not None:
            pets.extend(self.left.inorder())
        pets.append(self.pet)
        if self.right is not None:
            pets.extend(self.right.inorder())
        return pets

    def preorder(self):
        pets = [self.pet]
        if self.left:
            pets.extend(self.left.preorder())
        if self.right:
            pets.extend(self.right.preorder())
        return pets

    def postorder(self):
        pets = []
        if self.left:
            pets.extend(self.left.postorder())
        if self.right:
            pets.extend(self.right.postorder())
        pets.append(self.pet)
        return pets

    def count_by_breed(self):
        breeds = {}
        if self.left:
            for k, v in self.left.count_by_breed().items():
                breeds[k] = breeds.get(k, 0) + v
        breed = self.pet.breed
        breeds[breed] = breeds.get(breed, 0) + 1
        if self.right:
            for k, v in self.right.count_by_breed().items():
                breeds[k] = breeds.get(k, 0) + v
        return breeds

    def list_ids(self):
        ids = []
        if self.left:
            ids.extend(self.left.list_ids())
        ids.append(self.pet.id)
        if self.right:
            ids.extend(self.right.list_ids())
        return ids

    def report_by_location_and_gender(self):
        report = {}

        def infer_gender(name):
            return "Hembra" if name[-1].lower() == "a" else "Macho"

        def traverse(node):
            if not node:
                return
            location = node.pet.location.capitalize()
            gender = infer_gender(node.pet.name)
            if location not in report:
                report[location] = {"Macho": 0, "Hembra": 0}
            report[location][gender] += 1
            traverse(node.left)
            traverse(node.right)

        traverse(self)
        return report


class NodeAVL(NodeABB):
    def __init__(self, pet: Pet):
        super().__init__(pet)
        self.height = 1
        self.balance = 1