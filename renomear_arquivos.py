#import OS module to list and recognize folders and files
import os

#indicate the path of the folder containing the files
os.chdir('C:/testes/mail')

#variable that will count +1 after each rename
i=1

#inform the new name and file extension in dst
for file in os.listdir():
    src = file
    dst = "email" + str(i) + ".msg"
    os.rename(src, dst)

#the variable will add +1 after the new name informed above
    i+=1
