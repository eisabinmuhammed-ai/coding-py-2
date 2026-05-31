class my_class:
    __privetvar=27
    def __privmeth(self):
        print("I am in side my class")
    def hello(self):
        print("Privet var vaule : ",my_class.__privetvar)
foo=my_class()
foo.hello
foo.__privmeth
