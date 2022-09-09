
sqlcource=["oracle","sql","plsql","mangodb"] #list
courses={"course1":"python","course2":"selenium","course3":sqlcource} #dictonary
print(courses)
print(type(courses))
print(len(courses))
for eachvalue in sqlcource: # retreve the value from list
    print(eachvalue)
print(courses["course1"]) # retreive the value from dictonary
print(courses["course2"])
for eachvalue in courses["course3"]: # retreve the value from list
    print(eachvalue)
print(courses.get("course6")) # retreive the value from dictonary and it will return none when the key not exist
print(courses.keys()) # to get all the keys
for eachvalue in courses.keys():
    print(courses.get(eachvalue))
print(courses.values()) # to get all the values
for eachvalue in courses.values():
    print(eachvalue)
print(courses.items())
if "course4" in courses:
    print("Yes !!  its avaialbe")
else:
    print("No! we dont have")
print(courses["course2"]) #Update or add
courses["course9"]="Java" #add
print(courses)
courses.update({"course8":"C#"}) #add
print(courses)
courses.pop("course9") # delete the particular key
print(courses)
courses.popitem() # delete the last item in dictonary
print(courses)
del courses["course2"]
print(courses)
#del courses

newcourse=courses.copy()
courses.clear()
print(courses)
print(newcourse)

for key,val in newcourse.items():
    print(key,val)
fruits=("apple","ootty apple","kashmir apple")
price =200

appleprice=dict.fromkeys(fruits,price)
print(appleprice)
courses.setdefault("course2",".Net")
print(courses)





