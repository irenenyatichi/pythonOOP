class Car:
    def __init__ (self,make,color,model,mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.color = color
    def speed(self):
        return  f"Your car is a {self.make} of model {self.model}. It is color {self.color} with a mileage of {self.mileage}." 
    def engine(self):
        return  f"Your car is a {self.make} of model {self.model}. It is color {self.color} with a mileage of {self.mileage}."