from BasicsinPython.Vechicle import vechile


class Bike(vechile):

    def Manufactured(self): # this is not overriding
        print("Manufactured on 2022")

    def Model(self):
        print("Yamaha R15")

    def Max_speed(self): # overriding
        print("Max speed should be 120")

obj=Bike()
obj.Manufactured()
obj.Model()
obj.color()
obj.Max_speed()