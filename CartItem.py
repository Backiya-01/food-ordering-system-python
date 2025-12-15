class CartItem:
    def __init__(self, food_item, quantity):
        self.food_item = food_item
        self.quantity = quantity

    @property
    def total_price(self):
        return self.food_item.Price * self.quantity
