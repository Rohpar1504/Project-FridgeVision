from shopping_list import ShoppingList
from food import FoodItem

class Fridge:
    #Constructor
    def __init__(self):
        self.items = []
        self.shopping_list = ShoppingList()
        self.recipes = []

    #Adds an item to the fridge (maybe able to add to specific compartments later?)
    def add_item(self, item, quantity):
        item = FoodItem(self.name, quantity, self.expiration_date)
        if (item in self.items):
            #update the quantity of an existing item
            self.items[self.items.index(item)].quantity += item.quantity
        else:
    def add_item(self, item, quantity, expiration_date):
        item = FoodItem(name, quantity, expiration_date)
        found = False
        for existing_item in self.items:
            if existing_item.name == name:
                # Update quantity of existing item if it already exists
                existing_item.quantity += quantity
                found = True
                break
        if found == False:
            self.items.append(item)
            print('Added {item} to the fridge')

    #Removes an item from the fridge
    def remove_item(self, name, quantity):
        enough = False
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    enough = True
                    item.quantity -= quantity
                    print('Removed {quantity} of {item} from the fridge')
                    #Gets rid of the item on the list so we dont have apples quantity zero for example
                else:
                    item.quantity = 0
                if item.quantity == 0:
                        self.items.remove(item)
                        self.shopping_list.add_item(name)
        if (not enough):
            print('There is not enough of {item} in the fridge')
                    return
                else:
                    print('There is no {item} in the fridge')
    #Prints out all items in the fridge
    def list_items(self):
        if self.items:
            print('Items in the fridge:')
            for item in self.items:
                print('{item}')
        else:
            print('empty')