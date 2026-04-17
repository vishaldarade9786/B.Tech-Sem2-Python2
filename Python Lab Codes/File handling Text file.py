file=open("sample.txt","w")
file.write("Hii my name is Toast")
file.close

#2.read the file
file=open("sample.txt","r")
data=file.read()
print(data)
file.close()

#3.append the file
file=open("sample.txt","a")
file.write("\nwelcome to python")
file.close()
