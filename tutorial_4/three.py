class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ${self.price}")


car1 = Car("BMW", 2022, 29000)
car2 = Car("Honda Civic", 2021, 22000)

car1.cost()
car2.cost()