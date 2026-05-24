class person(object):
    def __init__(self,name,idnumber):
        self.name=name 
        self.idnumber=idnumber
    def deplay(self):
        print(self.name)
        print(self.idnumber)
class employ(person):
    def __init__(self,name,idnumber,salery,post):
        self.salery=salery
        self.post=post
        person.__init__(self,name,idnumber)
a=employ("ruhl",42372,8354,"ceo")
a.deplay()