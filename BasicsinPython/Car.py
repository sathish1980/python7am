from BasicsinPython.Vechicle import vechile


class car(vechile): # Single Inheritance

    def car_model(self):
        print("The car model is Benz")

    def Manufactured(self):
        print("Maufactured on 2000")

    def fuel_capacity(self):
        print("Max fuel capacity for Benz is 40")

    def Max_speed(self):
        print("Benz max speed is 200")

obj=car()
obj.car_model()
obj.Manufactured()
obj.color()
obj.fuel_capacity()
obj1=vechile()
obj1.Max_speed()
