class Textfileread():
    a=10
    fruits=("apple","orange","banana")

    def txtread(self):
        txrfile=open("C:\\Users\\sathishkumar\\PycharmProjects\\Python7AMBesantOnline\\Inputfile\\NEwWnv.txt")
        writefile = open("C:\\Users\\sathishkumar\\PycharmProjects\\Python7AMBesantOnline\\Inputfile\\newfile.txt","w")
        #print(txrfile.read(10))
        #print(txrfile.readline())
        #print(txrfile.readlines())
        listofvalue = txrfile.readlines()
        for eachros in listofvalue:
            print(eachros)
            writefile.write(eachros)

        writefile.write("This is sathish by entering automatic")
        txrfile.close()
        writefile.close()

obj=Textfileread()
obj.txtread()