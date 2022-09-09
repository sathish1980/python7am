from BasicsinPython.Encapsulation import Encapsulation


class encapinsul(Encapsulation):

    def Lorry(self):
        print(obj.__maxspeed)
        print(obj._pertrolcapacity)
        print(obj.a)
        print(obj.c)
        #print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

obj=encapinsul()
obj.setMaxSpeed(100)
obj.Lorry()
