class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        if name not in self.items:
            self.items.append(name)
            print('Added {name} to your shopping list!')
        else:
            print("{name} is already on your shopping list.")

    def remove_item(self, name):
        if name in self.items:
            self.items.remove(name)
            print('Removed {name} from your shopping list.')
        else:
            print("{name} is not on your list.")

    def print_items(self):
        if self.items:
            print('Shopping list items:')
            for item in self.items:
                print(item)
        else:
            print('Your shopping list is empty')