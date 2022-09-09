class collectionconecpt():

    def listconcept(self):
        fruits=["Apple","Orange","Mango","pineapple","cherry","mulberry","Apple"] # addd in to the list
        seasonalfruit=["mangostan"]

        age=[12,23,56,67,"apple","orange"]
        print(fruits)
        print(fruits[0]) # retrieve
        print(fruits[1])
        print(fruits[2],fruits[3])
        #print(fruits[3])
        for x in age:
            print(x)
        for x in range(0,len(fruits)):
            print(fruits[x])
        #last value
        print(fruits[-1])
        print(fruits[2:4])

        if "Pineapple" in fruits:
            print("it exist")
        else:
            print("Its not exist")

        for x in fruits:
            if x == "pineapple":
                print("it exist")
                break
            else:
                print("Its not exist")
#update the value in to list
        fruits[-1]="blueberry"
        print(fruits)
        fruits[1:4]=["chikku","dragon","melon"]
        print(fruits)
#insert
        fruits.insert(100,"musk melon")
        print(fruits)
        fruits.insert(5, "plums")
        print(fruits)
#append
        fruits.append("butter fruit")
        print(fruits)
#combine two list
        fruits.extend(seasonalfruit)
        print(seasonalfruit)
        print(fruits)
#delete
        fruits.remove("blueberry")
        print(fruits)
        fruits.pop()
        print(fruits)
        fruits.pop(-3)
        print(fruits)
        del fruits[-1]
        print(fruits)
        #del fruits
        #print(fruits)
#clear
        #fruits.clear()
        print(fruits)
#sorting
        fruits.sort()
        print(fruits)
        fruits.sort(reverse=True)
        print(fruits)
#copy a list
        latest=fruits.copy()
        print(latest)

    def tupleconept(self):
        fruits = ("Apple", "Orange", "Mango", "pineapple", "cherry", "mulberry", "Apple")  # addd in to the list
        seasonalfruits = ("mangostan","grapes")
        age=(1,2,3,4,5)
        condition=(True,False,True)
        print(fruits)
        print(fruits)
        print(fruits[0])  # retrieve
        print(fruits[1])
        print(fruits[2], fruits[3])
        for x in fruits:
            print(x)
        for x in range(2,len(fruits)):
            print(fruits[x])
        print(type(fruits))
        course=(("selenium","python","manual"),("selenium","java","manual"))
        print(course)
        print(course[0])
        for x in course[0]:
            print(x)
        print(fruits)
        print(fruits[-1])
        print(fruits[1:4])
        if "pineapple" in fruits:
            print("it exist")
        else:
            print("Its not exist")
        fruits=tuple(fruits)
        #seasonalfruit=tuple(seasonalfruit)

        fruits+=seasonalfruits
        print(fruits)
        #del fruits
        print(fruits.index("Apple"))
        print(fruits.count("Apple"))

obj=collectionconecpt()
obj.tupleconept()