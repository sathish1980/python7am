class classconcpet():

    global a,tax,name
    a=50
    tax=0.4
    name="sathish"
    first_name="kumar"
    First_name = "sathish"

    def __init__(self):
        print("this is constructor")




    def incometax(self,income):
        if(income<1000):
            self.tax=.1
            Asection=40
            Bsection=40
            Csection=40
            #or
            Asection,Bsection,Csetcion=40

            Tamil=30
            English=50
            Maths=90
            #or
            Tami,English,Maths=30,50,90
            taxtopercentagure=income*self.tax
            taxcal=income+taxtopercentagure
            print("with in 1000: "+ str(taxcal))
        else:
            self.name="Besant"
            taxtopercentagure = income * tax
            taxcal = income + taxtopercentagure
            print(taxcal)
            print(self.name)
    def studentdetails(self,name):
        self.a=30
        b=20 # b-is a variable and 20 is the value when u call b you will get a value of 20 #local variable
        b=70
        print("Welcome "+name +" to Python selenium course !!!")
        print(self.a)
        print(a)
        print(b)

    def anotherfunction(self):

        print("test")

    def assignmentoperator(self):
        a=9
        b=5
        c=20
        fruits=["apple","banana","orange"]
        print("intial value: " +str(a))
        #a=a+5
        a+=5
        print("after a addition of 5 is "+ str(a))
        print(a == b)
        print(a != b)
        a=b
        print(a)
        print(a>=b)
        print(not(a>10 and b<10 or c==30))
        print("apples" not in fruits)

    def ifcondition(self,age,country):
        if age>=18 and country=="IN":
            print("You are eligible to apply voter id")
            if age>=60:
                print("you are elib=gible for senior consession")
                if age >80:
                    print("you are eligible for super senior consession")
        elif age>15 and country=="IN":
            waitperiod = 18 - age
            print("You are  eligible for pre voter id. but to get an actual voter id you have to wait for " + str(waitperiod) + " more years")
        elif age > 12 and country=="IN":
            waitperiod = 18 - age
            print("You are  awaiting for pre voter id. but to get an actual voter id you have to wait for " + str(
                waitperiod) + " more years")
        else:
            waitperiod=18-age
            print("You are not eligible to apply voter id . please wait for " +str(waitperiod)+" more years")

    def gender(self,genderValue):
        #actualgender =""
        if genderValue == "F":
            print("You are Female")
            actualgender="Female"
        elif genderValue == "M":
            print("You are male")
            actualgender = "Male"
        elif genderValue == "T":
            print("You are Transgender")
            actualgender = "Transgender"
        else:
            print("This key word is not recogonized . please give F ,M or T")
            actualgender = ""
        return actualgender

    def genderidentification(self,genderkeywrd):
        actualgendername=clsobj.gender(genderkeywrd)
        print(actualgendername)

    def print100(self,intialvalue,endvalue):
       while intialvalue <= endvalue:
           intialvalue = intialvalue + 2
           if intialvalue == 300:
               continue
           print(intialvalue)

    def forloop(self,intial,endvalue):
        fruits=["apple","Orange","pineapple","Melon"]
        for eachvalue in fruits:
            print(eachvalue)
            for eachvalue1 in range(intial,endvalue+1):
                if eachvalue1 == 150:
                    break
                print(eachvalue1)
            if eachvalue == "pineapple":
                break



clsobj=classconcpet() #object
clsobj.studentdetails("sathish")
clsobj.anotherfunction()
clsobj.incometax(1500)
clsobj.assignmentoperator()
clsobj.ifcondition(85,"EN")
clsobj.genderidentification("T")
clsobj.print100(100,500)
clsobj.forloop(10,15)