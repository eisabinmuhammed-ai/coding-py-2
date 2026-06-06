class india():
    def capetel(self):
        print("new deli is my capetel")
    def langig(self):
        print("Hindi in spoke most ")
    def typy(self):
        print("India os a developing contry")

class Usa():
    def capetel(self):
        print("d.c. is my capetel")
    def langig(self):
        print("Engelsh in spoke most ")
    def typy(self):
        print("India os a develop contry")
obj_ind=india()
obj_us=Usa()
for contry in (obj_ind,obj_us):
    contry.capetel()
    contry.langig()
    contry.typy()
    
        