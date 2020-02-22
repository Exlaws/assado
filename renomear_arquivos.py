import os
os.chdir('C:/testes/mail')
i=1
for file in os.listdir():
    src = file
    dst = "email" + str(i) + ".msg"    
    os.rename(src, dst)
    i+=1