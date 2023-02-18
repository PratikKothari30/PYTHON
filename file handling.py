#Mode will define what we can do with the file like Read or Write

'''
f = open("gaurav.txt","w")
print("name of file: ",f.name)
print("file mode ",f.mode)
print("readble ",f.readable())
print("writable ", f.writable())
print("file has closed",f.closed)
f.close()
print("file has closed ", f.closed)
'''

# Performing write operation

'''
f = open("random.txt","a")
f.write("\n I am the best")
f.close()
print("file operation is done")
'''

#Inserting List

'''
f = open("gaurav.txt","w")
mylist = ["Gaurav","Jha","Something"]
f.writelines(mylist)
f.close()
print("Written work has done succesfully")
'''

# Reading data from a file


'''
f = open("covid.txt","r")
# print(f.read())
print(f.read(5))
print(f.readline())  #This will run the first line of the text file
print(f.readlines()) #This will return all the line of txt file in the form of List
f.close()
'''


# Reading and writing binary data


'''
with open("mytextfile","w") as f:
    f.write("Gaurav\n")
    f.write("Jha\n")
    f.write("Something\n")
    print("file closed: ", f.closed)
    
print("file closed", f.closed)
'''

# tell(),seek() and method working

'''
f= open("covid.txt","r")
print("total data=", f.read())
print("current position of coursor", f.tell())
f.seek(5) #From this point the txt file will start
print("the current position of cursor", f.tell())
print(f.read())
f.close()
'''

# Reading and Writing binary data

f1 = open("jha.jpg","rb")
f2 = open("Rossom.jpg","wb")
data = f1.read()
f2.write(data)
print("New Image is available with the name: ")
