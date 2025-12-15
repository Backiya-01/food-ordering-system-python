from AbstractItem import AbstractItem
from Foodmenu import Foodmenu

class Restaurant(AbstractItem):
    def __init__(self, name, rating, location, offer):
        super().__init__(name=name, rating=rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenu = []   # private variable

    @property
    def FoodMenu(self):
        return self.__FoodMenu

    @FoodMenu.setter
    def FoodMenu(self, Menu):
        for menu in Menu:
            if not isinstance(menu, Foodmenu):
                print("Invalid FoodMenu..")
                return
        self.__FoodMenu = Menu  # must be __FoodMenu

