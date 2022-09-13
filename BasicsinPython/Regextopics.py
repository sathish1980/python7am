import re


class regexvalidation():

    name ="This is sathish trainer"
    def regexcheck(self):
        r1 = re.findall(r"^\w+", self.name) #  get the first value
        print(r1)
        print(re.split(r"\s", self.name))  # get the first value
        print(re.split(r"s", self.name))  # get the first value


obj= regexvalidation()
obj.regexcheck()
