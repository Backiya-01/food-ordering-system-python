class Payment:
    def process(self, amount):
        print("\n💳 PAYMENT OPTIONS")
        print("1. UPI")
        print("2. Card")
        print("3. Cash on Delivery")

        choice = input("Select payment method: ")

        if choice in ["1", "2", "3"]:
            print(f"Payment of ₹{amount} successful")
            return True
        else:
            print("Payment failed")
            return False
