class listconcept():
    name="sathish"
    fruits=["apple","orange","pineapple","apple","plums","banana"]  # define a list
    age=[1,2,4,5,6]
    all=[1,2,3,4,"sathish","kumar","B.tech"]
    print(fruits)
    print(name)
    print(fruits[0]) # indexing
    print(fruits[1])
    print(fruits[-1])
    print(len(fruits))
    for eachvalue in fruits:
        print(eachvalue)
    # or
    for eachvalue in range(0,len(fruits)):
        print(fruits[eachvalue])
    #print(fruits[9])
    print(all)
    print(type(fruits))
    print(fruits[2:5])
    print(fruits[2:])
    if "pineapple" in fruits: # value exist in the list
        print("Yes its avaialble in the list")
    else:
        print("Its not avaiable")
    # update
    fruits[4]="Grapes"
    print(fruits)
    fruits[-1] = "Green Banana"
    print(fruits)
    fruits[2:4]=["PINEAPPLE","APPLE"]
    print(fruits)

    # insert
    fruits.insert(4,"Chiku")
    print(fruits)
    fruits.insert(10, "jackfruit")
    print(fruits)

    #append

    fruits.append("Mango")
    print(fruits)
    fruits.append("Gauva")
    fruits.append("Butterfruit")
    fruits.append("Dragon")
    print(fruits)
    #fruits.extend(age)
    print(fruits)

    # remove
    fruits.remove("Gauva")
    fruits.remove("Butterfruit")
    fruits.remove("Dragon")
    print(fruits)
    fruits.pop(-7)
    fruits.pop(4)
    print(fruits)
    fruits.pop()
    print(fruits)
    del fruits[4]
    print(fruits)
    #del fruits
    #print(fruits)
    #fruits.clear()
    print(fruits)
    fruits.sort()
    print(fruits)
    fruits.sort(reverse=True)
    print(fruits)
    newfruits=fruits.copy()
    print(newfruits)


