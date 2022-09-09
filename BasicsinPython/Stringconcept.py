class stringconcept():

    def stringhandle(self):
        namenew="sathishkumar"
        name=" sathish kumar's is a trainer "
        name1 = " Sathish kumar's is a trainer "

        Institue='Besant Technologies'
        FileName="sathishkumar.txt"
        print(name)
        print(Institue)
        print(len(name))
        #get each character from a string
        for each in range(0,len(name)):
            print(name[each])
        #get the no of chareacters in a string
        totalcharacter=len(Institue)
        print(totalcharacter)
        Tainerexist= "is a" in name
        print(Tainerexist)
        # to check no of T character in a name varaible
        count=0
        for each in range(0, len(name)):
            if (name[each])=='z':
                count+=1
        print("The given T present this many time",count)
        # not exist
        tainerdoesnotexist = "z" not in name
        print(tainerdoesnotexist)
        #Print a specific posistion vlaue
        totllen=len(FileName)
        actualvalue=FileName[2:totllen]
        print(actualvalue)
        #print(FileName[7:11])
        print(FileName[len(FileName)-4:totllen]) # FileName[7:11]
        print(FileName.upper())
        print(FileName.lower())
        print(name)
        print(name.strip())
        print(name.lstrip())
        print(name.rstrip())
        print(name.replace("sat","SAT"))
        print(name.split("ish"))
        print(name.split(' '))
        print(name+Institue)
        testindoublecoats="sathish kumar is a \"Tainer\""
        print(testindoublecoats)
        print(FileName.capitalize())
        print(FileName.isnumeric())
        print(FileName.count("x"))
        print(FileName.startswith("sathish"))
        print(FileName.endswith("xs"))
        print(FileName.rfind("x"))
        characterposstion=FileName.rfind(".")
        Filename=FileName[characterposstion+1:len(FileName)]
        if Filename=="xlxs":
            print("its an excelfile")
        elif Filename=="txt":
            print("it is an text file")
        print(FileName[characterposstion+1:len(FileName)])
        print("sathishkumar") # o/p
        print("ramukhsihtas") #o/p
        print("I am a trainer")
        print("I am a  reniart") #o/p"""
        print("applee") #op/ p-2 , e-2
        print(name.lower() == name1.lower())
        print(namenew)
        totallen = len(namenew)
        """for eachvalue in range(len(namenew)-1):
            print(namenew[totallen])
            totallen=totallen-1"""
        i=0
        print(totallen)
        actaullen=totallen-1
        while (totallen>0):
            print(namenew[totallen-1])
            totallen=totallen-1




obj=stringconcept()
obj.stringhandle()