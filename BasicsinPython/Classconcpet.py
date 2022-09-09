class classconceptsnew():
    global a,A
    a =50
    A=40
    b=30
    def mul(self,b=4):
        #a=30
        self.a=40
        #self.a=self.a+2
        self.a += 2
        c=self.a*b
        print("multiple", c)
        print(A)

    def div(self):
        #a=15
        b=3
        c=a/b
        print(int(c))

abc=classconceptsnew()
abc.mul(7)
abc.div()