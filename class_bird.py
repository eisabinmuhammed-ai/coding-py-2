class parrot:
    specec="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

woo=parrot("woo",14)
ble=parrot("ble",12)
print("woo is a {}".format(woo.specec))
print("ble is a {}".format(ble.specec))
print("{} is {} old ".format(woo.name,woo.age))
print("{} is {} old ".format(ble.name,ble.age))