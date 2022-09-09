from BasicsinPython.BaseBank import BaseBank


class HDFCLoans(BaseBank):

    def homeinterestRate(self):
        homeinterestrate=0.06
        print("Your home loan percentage is : ",homeinterestrate)

    def Personalloaninterest(self):
        personalinterestrate=0.10
        print("Your personal loan percentage is : ",personalinterestrate)

obj=HDFCLoans()
obj.homeinterestRate()
obj.Personalloaninterest()
