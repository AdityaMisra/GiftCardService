from models.basket import Basket


class Customer:
    def __init__(self, name):
        self.name = name
        self.basket = Basket(self)

    def add_gift_card(self, gift_card):
        return self.basket.add_item(gift_card)

    def get_total_basket_price(self):
        return self.basket.get_total_cost()
