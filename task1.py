class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: \nBrand: {self.brand} \nModel: {self.model} \nYear: {self.year}")

car1 = Car("Supra", "MK5", 2019)
car2 = Car("Honda", "Civic", 2022)

car1.display_info()
car2.display_info()
