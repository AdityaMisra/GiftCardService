class GiftCard:
    def __init__(self, brand, face_value):
        self.brand = brand
        self.face_value = face_value
        self.cost = self.get_cost()

    def get_cost(self):
        return self.face_value * ((100-self.brand.discount)/100)
