class ExceptionHandling():
    a=10
    b=20
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)

    def div(self,a,b):
        try:
            c=a/b
            print(c)
        except ZeroDivisionError:
            print("Zero division error")
        except:
            print("exception")
        finally:
            print("finally block")

    def anotherfun(self,a,b):
        c=a/b
        if c >= 2:
            raise ZeroDivisionError("Exception raised by user")
        print(c)



obj=ExceptionHandling()
obj.anotherfun(10,2)
obj.add()