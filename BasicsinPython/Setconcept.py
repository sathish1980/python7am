class setconcpet():

    fruits={"apple","banana","pineapple","berry","apple"}
    summerfruits={"Mango","Red Banana","apple","gauva"}
    print(fruits)
    for eachvalue in fruits:
        print(eachvalue)
    #add a value
    fruits.add("butterfruit")
    fruits.add("grapes")
    fruits.add("plums")
    print(fruits)
    #update
    #fruits.update(summerfruits)
    print(fruits)
    #remove
    fruits.remove("berry")
    fruits.remove("banana")
    print(fruits)
    #fruits.pop()
    print(fruits)
    fruits.discard("apples")
    print(fruits)
    #fruits.clear()
    print(fruits)
    #del fruits
    print(fruits)
    #difference
    print(summerfruits)
    x=fruits.difference(summerfruits)
    print(x)
    print(fruits)
    print(summerfruits)
    #y = summerfruits.difference(fruits)
    #print(y)
    #fruits.difference_update(summerfruits)
    print(fruits)
    print(summerfruits)
    #intersection
    x = fruits.intersection(summerfruits)
    #print(x)
    #fruits.intersection_update(summerfruits)
    #print(fruits)
    #x=summerfruits.issubset(fruits)
    #print(x)
    x=fruits.symmetric_difference(summerfruits)
    print(x)
    fruits.symmetric_difference_update(summerfruits)
    print(fruits)
    x = fruits.issuperset(summerfruits)
    print(x)





