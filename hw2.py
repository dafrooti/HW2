class Car:
    def __init__(self, color, brand, model):

        self.color = color
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, color, brand, model, battery_capacity):

        super().__init__(color, brand, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print("Car is charging")


my_car = Car("Red", "Toyota", "Camry")


print("Color:", my_car.color)



my_electric_car = ElectricCar("Blue", "Tesla", "Model S", "100 kWh")


print("Color:", my_electric_car.color)
print("Battery Capacity:", my_electric_car.battery_capacity)

my_electric_car.charge()