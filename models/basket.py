from models.giftcard import GiftCard


class Basket:
    def __init__(self, customer):
        self.customer = customer
        self.gift_cards = []

    # total_cost of the basket
    def get_total_cost(self):
        total_cost = 0.0
        for each_gc in self.gift_cards:
            total_cost += each_gc.get_cost()

        return total_cost

    # add item to the basket
    def add_item(self, gift_card):
        if not isinstance(gift_card, GiftCard):
            raise ValueError("Invalid gift card. Please try again.")

        self.gift_cards.append(gift_card)

        return self.get_total_cost()
