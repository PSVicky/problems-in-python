file1 = open("text1.txt","r")
file_content = file1.read()
print(file_content)
file1.close()

with open("text1.txt","w") as file1:
    txt = "Vicky is the disiple and obidence boy who always wont talk with girls and become the best in sports and to become the best programmer in his college"
    file1.write(txt)
    
with open("text1.txt","a") as file1:
    txt = "\nGowtham has completed his higher and he want to become an software developer so he need to study an computer science and engineering to be the best computer science engineer"
    file1.write(txt)
    
   
    