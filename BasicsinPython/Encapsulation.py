class Encapsulation:

    global c
    c=20
    a=10 #public
    _pertrolcapacity=20 #protected
    __maxspeed = 0 #private
    __name = ""

    def __int__(self):
        pass
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def accesmodifier(self):
        print("the petrol capacity is : ",self._pertrolcapacity)
        print("the a value is : ", self.a)




redcar = Encapsulation()
redcar.drive()
redcar.accesmodifier()