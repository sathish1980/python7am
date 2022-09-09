from BasicsinPython.sample import sample


class processed(sample):

    def process1(self):
        c=obj.a+obj.b
        print(c)

obj=processed()
obj.process()
obj.process1()
