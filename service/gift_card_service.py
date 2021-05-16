from models.brand import Brand
from models.customer import Customer
from models.giftcard import GiftCard


class GiftCardService:
    """
    1. multiple customers can add multiple types of gc to basket
    2. total price of the basket
    3. customer's basket should get updated on change of price
    """
    @staticmethod
    def run():
        # create brands
        apple = Brand("Apple", 5)
        walmart = Brand("Walmart", 15)
        amazon = Brand("Amazon", 10)

        # create gift cards
        apple_gc_50 = GiftCard(apple, 50)
        apple_gc_25 = GiftCard(apple, 25)
        walmart_gc = GiftCard(walmart, 100)
        amazon_gc = GiftCard(amazon, 20)

        # create customers
        customer_a = Customer("A")
        customer_b = Customer("B")

        print("customer_a Add apple - ", customer_a.add_gift_card(apple_gc_50))
        print("customer_a Add amz - ", customer_a.add_gift_card(amazon_gc))
        print("customer_a Total cost - ", customer_a.get_total_basket_price())

        print("customer_b ", customer_b.add_gift_card(walmart_gc))
        print("customer_b ", customer_b.add_gift_card(apple_gc_25))
        print("customer_b ", customer_b.add_gift_card(amazon_gc))
        print("customer_b Total cost - ", customer_b.get_total_basket_price())

        print("customer_a Add apple - ", customer_a.add_gift_card(apple_gc_25))
        print("customer_a Total cost - ", customer_a.get_total_basket_price())

        amazon.update_discount(20)
        print("customer_a Total cost - ", customer_a.get_total_basket_price())
        print("customer_b Total cost - ", customer_b.get_total_basket_price())
