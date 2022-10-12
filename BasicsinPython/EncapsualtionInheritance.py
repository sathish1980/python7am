from BasicsinPython.Encapsulation import Encapsulation


class encapinsul(Encapsulation):

    newspeed=0

    def Lorry(self):
        print(obj.__maxspeed)
        print(obj._pertrolcapacity)
        print(obj.a)
        print(obj.getmaxspeed(750))
        newspeed=obj.getmaxspeed(750)
        print(newspeed)

        #print(obj.c)
        #print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

obj=encapinsul()
obj.setMaxSpeed(100)
obj.Lorry()
