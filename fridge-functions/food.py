class FoodItem:
    #Constructor
    def __init__(self, name, quantity, expiration_date):
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date
    def is_expired(self):
        #Time?