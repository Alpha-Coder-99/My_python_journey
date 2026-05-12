# Question#02:Write a program to read a text from a given file certificate.txt and find whethr it contains the word happy
f=open("Chap#20(File Handling)/certification.txt","r")
dataOfFile=f.read()
dataOfFile=dataOfFile.lower()
if"happy"in dataOfFile:
    print("Yes!word 'happy' exists in file ")
else:
    print("No!word 'happy' not exists in file ")
f.close()