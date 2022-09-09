class ifconditions():

    def voterid(self,age,country):
        if age >= 18 and country =="IN":
            print("You are eligible to apply voter id")
            if age >60:
                print("you are eligible to senior citizen")
                if age >80:
                    print("you are eligible for super senior citizen")
        elif age>15 and age< 18:
            print("you are eligible to apply prevoter id")
            waitperiod = 18 - age
            print("You are not eligible to apply voter id please wait for ", waitperiod, "More years")
        elif age>12 and age< 18:
            print("you are not eligible to apply prevoter id")
            waitperiod = 15 - age
            print("You are not eligible to apply pre voter id please wait for ", waitperiod, "More years")
        else:
            waitperiod=18-age
            print("You are not eligible to apply voter id please wait for ",waitperiod,"More years")
        if age>18:
            pass
        else:
            pass

    def whileloop(self,intial):
        additionof10value =intial
        additionof10value +=10
        while intial <= additionof10value:
            intial +=1
            if(intial==55):
                continue
            print(intial)

    def forloopconcpet(self):
        fruits=["apple","orange","mango"]
        count=[1,2,3,4]
        print(fruits)
        for eachvalue in fruits:
            for numbervalue in count:
                print(numbervalue)
                if(eachvalue == "orange"):
                    continue
                print(eachvalue)

    def div(self,number):
        try:
            a=10
            c=a/number
            print("The division of number is: ",c)
        except ZeroDivisionError:
            print("There is an zero division error ")
        except:
            print("There is an exception")
        finally:
            print("finally is executed")

    def divwithexception(self, number):
            if number == 0:
                raise ZeroDivisionError("Hi you have entered 0 value division")
            else:
                a = 10
                c = a / number
                print("The division of number is: ", c)
obj=ifconditions()
obj.divwithexception(3)
obj.voterid(85,"ENG")
obj.whileloop(51)
obj.forloopconcpet()
