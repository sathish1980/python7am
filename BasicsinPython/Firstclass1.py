print('sathish')
#print("kumar")
"""print("R")
print("B.tech")
print("Beasant Technologie's")"""
print("""Sathish kumar is a selenium python trainer"
      " and he has 3 years of expereince in training"
      " and also he has 10 + years of expereince in IT""")
print("""\"sathish\"""")
print("2"+"3")
print("The sum of two number is :" ,2+3 ,2*3 , "This is sathish")
print(2.10)

# We are adding two values
def add():
    a=10
    b=20
    c=a+b # we are adding two values
    print(c)
    d=True
    print(type(a))
    print(type(d))
print("afterfunction")
#We are subtracting 2 values
def subtraction(a,b):
    c = a - b  # we are adding two values
    print(c)
    e=div()
    print(e)
    print(e>15)
def sub(a=10,b=2):
    c=a-b #8 #25
    d=div() #1 #1
    e=c+d   #8+1 #26
    print("%%%%%%%%")
    print(c)
    print(e) #9
    f=const()
    print(f)
    g=mul(a,b)
    print(g)
    print("%%%%%%%%")


def div():
    a=20
    b=20
    c=b/a
    return c

def const():
    return 30

def mul(a,b):
    c=b*a
    return c

def datatype():
    a=10.45
    b=2.343
    c="sathish"
    d='cssa'
    e=True
    f=False
    g=["sathish","kumar","R"]
    h=("apple","bananna")
    v=type(a)
    print(v)
    print(a)
    print("****************")
    z=str(a)
    print(z)
    print(type(z))
    print("****************")
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
    print(type(h))


add() # functional call
sub(30,5)
datatype()
subtraction(3,7)
