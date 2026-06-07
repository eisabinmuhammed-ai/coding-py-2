class titel:
    def __init__(self,ather,titel,borrw):
        self.ather=ather
        self.titel=titel
        self.borrw=borrw
    def borrow(self):
         print("you have borrwed the book")
    def retur(self):
        b=input("did you return the book: ")
        if b == "no":
            print("retern the book tomorrw")
        else:
            print("thank you")

a=titel("daved willems","1",True)
c=a.borrw
print(a.borrow)
print("the ather of the book is {} the books name is {} and it is",c  ,"that you have borrowd the book",format(a.ather,a.titel))
a.retur

