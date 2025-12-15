from FoodManager import FoodManager
from Cart import Cart
from Order import Order
from Payment import Payment

class MainMenu:
    __options={1:"Show Restaurants",2:"Search Restaurants",3:"Search FoodItems",4:"View Cart",5:"Place Order",6:"Exit"}
    def __init__(self):
        self.manager=FoodManager()
        self.cart = Cart()

    def Start(self):
        while True:
            for Option in MainMenu.__options:
                print(f"{Option}.{MainMenu.__options[Option]}",end="  ")
            print()
            try:
                choice=int(input("Please Enter Your Choice : "))
                Value=MainMenu.__options[choice].replace(" ","")
                getattr(self, Value)()


            except (ValueError,KeyError):
                print("Invalid input..Please Enter the Valid Choice")


    def ShowRestaurants(self):
        print("\nAvailable Restaurants:\n")
        for i, res in enumerate(self.manager.Restaurents, start=1):
            print(f"{i}.{res.Name} | Rating: {res.Rating} | Location: {res.Location}")

        try:
            choice = int(input("\nSelect Restaurant (0 to return to Main Menu): "))
            if choice == 0:
                return
            self.ShowFoodMenus(choice)
        except (ValueError, IndexError):
            print("Invalid choice")


    def ShowFoodMenus(self, res_index):
        restaurant = self.manager.Restaurents[res_index - 1]

        print(f"\nMenus in {restaurant.Name}:")
        for idx, menu in enumerate(restaurant.FoodMenu, start=1):
            print(f"{idx}. {menu.Name}")

        choice = int(input("\nSelect Menu: "))
        self.ShowFoodItems(restaurant, choice)
        input("\nPress Enter to return to Main Menu...")  

    def ShowFoodItems(self, restaurant, menu_index):
        menu = restaurant.FoodMenu[menu_index - 1]

        print(f"\nFood Items in {menu.Name}:")
        for i, item in enumerate(menu.FoodItems, start=1):
            print(f"{i}. {item.Name} | ₹{item.Price} | Rating {item.Rating}")

        try:
            choice = int(input("\nSelect item number to add to cart (0 to cancel): "))
            if choice == 0:
                return

            selected_item = menu.FoodItems[choice - 1]

            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be greater than 0")
                return

            # ✅ THIS LINE IS THE KEY
            self.cart.add_item(selected_item, qty)

        except (ValueError, IndexError):
            print("Invalid item selection")

    def SearchRestaurants(self):
        key = input("Enter restaurant name: ").lower()
        matches = []

        for res in self.manager.Restaurents:
            if key in res.Name.lower():
                matches.append(res)

        if not matches:
            print("No restaurants found.")
            return

        print("\nSearch Results:")
        for i, res in enumerate(matches, start=1):
            print(f"{i}. {res.Name} | {res.Location} | Rating {res.Rating}")

        try:
            choice = int(input("\nSelect restaurant to view menu (0 to cancel): "))
            if choice == 0:
                return
            selected_res = matches[choice - 1]
            self.ShowFoodMenusByRestaurant(selected_res)
        except (ValueError, IndexError):
            print("Invalid choice.")

    def ShowFoodMenusByRestaurant(self, restaurant):
        print(f"\nMenus in {restaurant.Name}:")
        for i, menu in enumerate(restaurant.FoodMenu, start=1):
            print(f"{i}. {menu.Name}")

        try:
            choice = int(input("Select menu: "))
            self.ShowFoodItems(restaurant, choice)
        except (ValueError, IndexError):
            print("Invalid menu choice.")
        

    def SearchFoodItems(self):
        key = input("Enter food name: ").lower()
        found = False

        for res in self.manager.Restaurents:
            for menu in res.FoodMenu:
                for item in menu.FoodItems:
                    if key in item.Name.lower():
                        print(
                            f"{item.Name} | ₹{item.Price} | Rating {item.Rating} "
                            f"\n → Restaurant: {res.Name} ({menu.Name})\n"
                        )
                        found = True

        if not found:
            print("No food items found.")


    def Exit(self):
        print("Thank you!")
        exit()


    def ViewCart(self):
        self.cart.show_cart()
        input("\nPress Enter to return...")

    def PlaceOrder(self):
        if not self.cart.items:
            print("Cart is empty. Add items first.")
            return

        order = Order(self.cart)
        order.show_summary()

        confirm = input("\nConfirm order? (y/n): ").lower()
        if confirm != "y":
            print("Order cancelled.")
            return

        payment = Payment()
        success = payment.process(order.total_amount)

        if success:
            order.status = "PAID"
            print("\n Order placed successfully!")
            self.cart.items.clear()
        else:
            print("Payment failed. Try again.")

