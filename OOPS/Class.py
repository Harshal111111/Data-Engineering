class Car:
  def __init__(self, model, make, year):
    self.model = model
    self.make = make
    self.year = year

  def display_info(self):
    return f"{self.year} {self.model} {self.make}"


car1 = Car("Toyota", "Camry", 2024)
print(car1.display_info())

class ElectricCar(Car):                     # Inheritence
  def __init__(self, make, model, year, battery_capacity):
    super().__init__(make, model, year)
    self.battery_capacity = battery_capacity

  def display_info(self):                               #poly
    return f"{self.year} {self.model} {self.make} with {self.battery_capacity} Kwh"


car2 = ElectricCar("Tata", "Curvvv", 2024, 100)
print(car2.display_info())


# This code is example of inheritance and polymorphism