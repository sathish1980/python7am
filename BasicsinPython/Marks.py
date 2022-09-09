from BasicsinPython.Students import Students


class Marks():


    def subjects(self):
        #print(Students.schoolname)
        print(self.schoolname) # or print(Src.schoolname)
        print("Tamil","Maths","English","Science")

    def Grades(self,percentage):
        if percentage>=90:
            Grade="A"
            print("You are belongs to Grade : A")
        elif percentage>=80:
            Grade="B"
            print("You are belongs to Grade : B")
        elif percentage>=70:
            Grade="C"
            print("You are belongs to Grade : C")
        elif percentage>=40:
            Grade="D"
            print("You are belongs to Grade : D")
        else:
            Grade="E"
            print("You are belongs to Grade : E")
        return Grade

    def OverallGrade(self,TamilMark,EnglishMark,MathsMark,scienecMark):
        TotalMark=TamilMark+EnglishMark+MathsMark+scienecMark
        print("Yout toal Mark is : ",TotalMark)
        Totalpercentage=(TotalMark/400)*100
        print("Your total percentage is: ",Totalpercentage)
        return self.Grades(Totalpercentage)

"""Src=Marks()
Src.subjects()
Src.studentDetails("markcard",34,978565)
Src.sportsDetails()
Src.OverallGrade(40,60,60,60)"""