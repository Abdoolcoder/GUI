class User:
    def sign_in(self):
        return f'u have been in'
    
class Car(User):
    def __init__(self,name):
        self.name = name

    def car_name(self):
        return f'the car name is {self.name}'
    
class bike(User):
    def __init__(self,name):
        self.name = name

    def bike_name(self):
        return f'the bike name is {self.name}'
    
bike1 = bike('Honda')
print(bike1.bike_name())
print(bike1.sign_in())
