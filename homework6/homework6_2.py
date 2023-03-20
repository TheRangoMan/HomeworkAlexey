from homework6_1 import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = []
    
    

stand = IceCreamStand("Stand")
stand.flavors.append("Choco")
stand.flavors.append("Vanilla")
stand.flavors.append("Frutty")
stand.flavors.append("Almond")

print(stand)
    