class revers:
    string1=input("enter string:  ")
    def __init__(self,torf):
        self.torf=torf
    def leter(self):       
        return self.torf
string=revers(True)
string2=string.torf
string3=string.string1
if string2 == True:
   
    string2=("")
    for i in string3:
        string2= i + string2
print("the reverst numbre is  ",string2) 