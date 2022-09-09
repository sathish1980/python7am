class loops():

    def forloop(self):
        fruits=["apple","orange","banana"]
        for eachvalue in range(10,21):
            print(eachvalue)

        for eachvalue in    fruits:
            print(eachvalue)

    def whileloop(self,i):
        while(i<10):
            print(i)
            i+=1
obj=loops()
obj.forloop()
obj.whileloop(2)