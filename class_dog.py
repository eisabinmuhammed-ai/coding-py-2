class dog:
    specec="dog"
    def __init__(self,coloer,hight):
        self.hight=hight
        self.coloer=coloer

dovermen=dog("black and white","28 inches")
chaw_chaw=dog("can be gray,black and orenge","17 inches")
print("dovermen is a {}".format(dovermen.specec))
print("chaw chaw is a {}".format(chaw_chaw.specec))
print("dovermen {} coloer and {} tall ".format(dovermen.coloer,dovermen.hight))
print("chaw chaw {} coloer and {} tall ".format(chaw_chaw.coloer,chaw_chaw.hight))