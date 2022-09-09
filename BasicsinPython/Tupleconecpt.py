class Tuple():
    fruits=("apple","banana","pineapple","apple","plums","grapes")
    summerfruits=("Mango","Red banana")
    print(fruits)
    print(fruits[0])#this is user the get the first value
    print(len(fruits)) # check the total values
    for eachvalue in fruits:
        print(eachvalue)
    for eachvalue in range(0,len(fruits)):
        print(fruits[eachvalue])
    print(fruits[-1]) # get the value from last
    print(fruits.count("apple"))
    print(fruits.index("pineapple"))
    print(type(fruits))
    print(fruits[2:5])
    #fruits[5]="butterfruit"
    print(fruits)
    convertintolist=list(fruits)
    print(type(convertintolist))
    print(convertintolist)
    convertintolist[5]="butterfruit"
    print(convertintolist)
    newtuple=tuple(convertintolist)
    print(newtuple)

    fruits+=summerfruits
    print(fruits)
    