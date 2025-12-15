class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, food_item, quantity):
        self.items.append((food_item, quantity))
        print(f"\n{food_item.Name} added to cart ({quantity})")

    def show_cart(self):
        if not self.items:
            print("\n Cart is empty")
            return

        print("\n Your Cart:")
        total = 0
        for item, qty in self.items:
            price = item.Price * qty
            total += price
            print(f"{item.Name} x {qty} = ₹{price}")

        print(f"\nTotal Amount: ₹{total}")
