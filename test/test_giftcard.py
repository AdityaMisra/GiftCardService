import pytest

from models.brand import Brand
from models.customer import Customer
from models.giftcard import GiftCard
from service.gift_card_service import GiftCardService


class TestGiftService:

    # def setup(self):
    #     # create brands
    #     apple = Brand("Apple", 5)
    #     walmart = Brand("Walmart", 15)
    #     amazon = Brand("Amazon", 10)
    #
    #     # create gift cards
    #     apple_gc_50 = GiftCard(apple, 50)
    #     apple_gc_25 = GiftCard(apple, 25)
    #     walmart_gc = GiftCard(walmart, 100)
    #     amazon_gc = GiftCard(amazon, 20)
    #
    #     # create customers
    #     customer_a = Customer("A")
    #     customer_b = Customer("B")

    def test_all(self):
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

        assert isinstance(customer_b, Customer)

        assert customer_a.add_gift_card(apple_gc_50) == 47.5
        # assert customer_a.add_gift_card(123) == 47.5
        assert customer_a.add_gift_card(amazon_gc) == 65.5
        assert customer_a.get_total_basket_price() == 65.5

        assert customer_b.add_gift_card(walmart_gc) == 85.0
        assert customer_b.add_gift_card(apple_gc_25) == 108.75
        assert customer_b.add_gift_card(amazon_gc) == 126.75
        assert customer_b.get_total_basket_price() == 126.75

        assert customer_a.add_gift_card(apple_gc_25) == 89.25
        assert customer_a.get_total_basket_price() == 89.25

        amazon.update_discount(20)
        assert customer_a.get_total_basket_price() == 87.25
        assert customer_b.get_total_basket_price() == 124.75

    def test_customer_instance(self):
        # create customers
        customer_b = Customer("B")
        assert isinstance(customer_b, Customer)

    @pytest.mark.parametrize("customer, gc, amount", [(Customer("A"), GiftCard(Brand("Apple", 5), 50), 47.5),
                                                      (Customer("A"), GiftCard(Brand("Amazon", 10), 20), 18),
                                                      (Customer("A"), GiftCard(Brand("Apple", 5), 25), 23.75),
                                                      (Customer("B"), GiftCard(Brand("Walmart", 15), 100), 85.0),
                                                      (Customer("B"), GiftCard(Brand("Apple", 5), 25), 23.75),
                                                      (Customer("B"), GiftCard(Brand("Amazon", 10), 20), 18),
                                                      ])
    def test_add_gift_card_parametrized(self, customer, gc, amount):
        assert customer.add_gift_card(gc) == amount

    def test_total_basket_amount(self):
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

        customer_a.add_gift_card(apple_gc_50)
        customer_a.add_gift_card(amazon_gc)
        assert customer_a.get_total_basket_price() == 65.5

        customer_b.add_gift_card(walmart_gc)
        customer_b.add_gift_card(apple_gc_25)
        customer_b.add_gift_card(amazon_gc)
        assert customer_b.get_total_basket_price() == 126.75

        customer_a.add_gift_card(apple_gc_25)
        assert customer_a.get_total_basket_price() == 89.25

        amazon.update_discount(20)
        assert customer_a.get_total_basket_price() == 87.25
        assert customer_b.get_total_basket_price() == 124.75

    def test_value_error(self):
        # create customers
        customer_a = Customer("A")

        with pytest.raises(ValueError):
            customer_a.add_gift_card(123)

    def test_gift_card_service(self):
        assert GiftCardService.run() is None
