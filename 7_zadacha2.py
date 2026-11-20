class Car: 
    def __init__(self, brand, horsepower): 
        self.brand = brand
        self.horsepower = horsepower
    def __str__(self): 
        return f'Автомобилът е марка {self.brand} и има {self.horsepower} конски сили'
car1 = Car('BMW', 200)
print(car1)