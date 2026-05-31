class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity


class Bus(Vehicle):
    def __init__(self, capacity, fare_per_passenger):
        super().__init__(capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self):
        basic_fare = self.capacity * self.fare_per_passenger
        maintenance_charge = basic_fare * 0.10
        return basic_fare + maintenance_charge


bus = Bus(50, 100)
print("Total Fare:", bus.calculate_total_fare())