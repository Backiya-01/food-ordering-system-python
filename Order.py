from datetime import datetime

class Order:
    def __init__(self, cart):
        self.items = cart.items
        self.date = datetime.now()
        self.total_amount = self.calculate_total()
        self.status = "CREATED"

    def calculate_total(self):
        total = 0
        for item, qty in self.items:
            total += item.Price * qty
        return total

    def show_summary(self):
        print("\n🧾 ORDER SUMMARY")
        for item, qty in self.items:
            print(f"{item.Name} x {qty} = ₹{item.Price * qty}")
        print(f"\nTotal Amount: ₹{self.total_amount}")
        print(f"Order Status: {self.status}")
