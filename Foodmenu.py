from AbstractItem import AbstractItem
from Fooditem import Fooditem
class Foodmenu(AbstractItem):
    def __init__(self, name):
        super().__init__(name=name)
        self.__FoodItems = []

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, Fooditem):
                print("Invalid FoodItem..")
                return
        self.__FoodItems = items
