from abc import ABC ,abstractmethod
class abs(ABC):
    def print(self,x):
        print("past value ",x)
    @abstractmethod
    def eask(self):
        print("We are in inside absclass")
class test_class(abs):
    def eask(self):
        print("We are in inside testclass")
test_ob=test_class()
test_ob.eask()
test_ob.print(425)