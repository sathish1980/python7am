from BasicsinPython.BaseBank import BaseBank
from BasicsinPython.Process import processed
from BasicsinPython.sample import sample


class SBILoans(BaseBank,sample):

    def homeinterestRate(self):
        homeinterestrate=0.07
        print("Your home loan percentage is : ",homeinterestrate)

    def Personalloaninterest(self):
        personalinterestrate=0.13
        print("Your personal loan percentage is : ",personalinterestrate)

SBIL=SBILoans()
SBIL.homeinterestRate()
SBIL.Personalloaninterest()
SBIL.process()