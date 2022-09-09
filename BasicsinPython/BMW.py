from BasicsinPython.Ferrrai import Ferrari


class BMW():
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print("Max speed is 240")
    def max_speed(self,a,b):
        print("Max speed is 260")

    def manufacture(self):
        print("manufactured in 2000")

"""obj=BMW()
obj.fuel_type()
obj.max_speed()
obj1=Ferrari()
obj1.fuel_type()
obj1.max_speed()"""

for eachobj in (BMW(),Ferrari()):
    eachobj.fuel_type()
    eachobj.max_speed()
    eachobj.manufacture()