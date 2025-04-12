from model.abb import ABB
from model.pet import Pet


class ABBService():
    def __init__(self):
        self.abb = ABB()
        # Llenar ABB
        self.abb.add(Pet(id=7, name="Lulu", age=13, breed="Pug", location="manizales"))
        self.abb.add(Pet(id=2, name="nene", age=5, breed="Pitbull", location="Chinchina"))

    def get_all(self):
        return self.abb.inorder()

    def delete(self, id: int):
        self.abb.delete(id)

    def average_age_by_gender(self):
        return self.abb.average_age_by_gender()

    def count_by_breed(self):
        return self.abb.count_by_breed()

    def get_ids(self):
        return self.abb.get_ids()

    def get_preorder(self):
        return self.abb.preorder()

    def get_postorder(self):
        return self.abb.postorder()

    def report_by_location_and_gender(self):
        return self.abb.report_by_location_and_gender()