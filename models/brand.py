
class Brand:
    def __init__(self, name, discount):
        """

        :rtype: object
        """
        self.name = name
        # value in percentage
        self.discount = discount

    def update_discount(self, new_discount):
        self.discount = new_discount
