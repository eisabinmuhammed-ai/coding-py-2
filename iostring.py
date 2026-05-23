class Iostring():
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input("emter string: ")
    def print_string(self):
        print("the result is ",self.str.upper())
ob=Iostring()
ob.get_string()
ob.print_string()