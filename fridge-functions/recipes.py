class Recipes:
    #Constructor
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.recipes = []
    #Adds a recipe
    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipes(name, ingredients, instructions)
        self.recipes.append(recipe)
        print("Recipe '{name}' added.")

    def check_ingredients(self, recipe):
        missing_ingredients = []
        for ingredient in self.ingredients:
            ingredient_name = ingredient[0]
            required_quantity = ingredient[1]
            found = False
            for item in fridge.items:
                if item.name == ingredient_name:
                    if item.quantity >= required_quantity:
                        found = True
                        break
            if found == False:
                missing_ingredients.append((ingredient_name, required_quantity))
        if missing_ingredients:
            print("Missing ingredients:")
            for ingredient in missing_ingredients:
                print("{ingredient[0]} Number: {ingredient[1]}")
                fridge.shopping_list.add_item(ingredient[0])
        else:
            print("All ingredients are in the fridge!")