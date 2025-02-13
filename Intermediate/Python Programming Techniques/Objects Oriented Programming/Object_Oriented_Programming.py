# A class to represent a car
class Car:
    def __init__(self, make, model, year):
        """
        Initialize a Car object with make, model and year.
        :param make: The make of the car (e.g. Toyota)
        :param model: The model of the car (e.g. Corolla)
        :param year: The year of the car (e.g. 2022)
        """
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        """
        Display the details of the car.
        """
        print(f"{self.year} {self.make} {self.model}")

# Create a Car object
my_car = Car("Toyota", "Corolla", 2022)

# Display the details of the car
my_car.display_details()

