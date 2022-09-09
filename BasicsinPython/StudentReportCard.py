from BasicsinPython.Marks import Marks
from BasicsinPython.Students import Students


class StudentreportCard(Marks,Students):

    def school(self):
        print(Students.schoolname)

    def SpecialclassExist(self,Grade):
        if Grade == "A":
            print("You are Top student")
        elif Grade == "B":
            print("You have to study little more")
        elif Grade == "C":
            print("You are average in studied . please concentrate more")
        elif Grade == "D":
            print("You just passed .please put more effort")
        else:
            print("You are Fail . you have a special class from Tomorrow")



Src=StudentreportCard()
Src.subjects()
Src.studentDetails("sathish",30,978565)
ActualGrade=Src.OverallGrade(90,90,90,92)
Src.SpecialclassExist(ActualGrade)
Src.school()

