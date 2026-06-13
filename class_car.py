class BMW:
    def __init__(self, model):
        self.model = model

    def fuel_type(self):
        return "Gasoline or Electric"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    def __init__(self, model):
        self.model = model

    def fuel_type(self):
        return "High-octane Gasoline"

    def max_speed(self):
        return "340 km/h"



car1 = BMW("M5")
car2 = Ferrari("SF90 Stradale")


for car in (car1, car2):
    print(f"--- {car.model} ---")
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")
    print()