from abc import ABC
class animel:
    def move(self):
        pass
class humen(animel):
    def move(self):
        print("I can walk and talk")
class snake(animel):
    def move(self):
        print("I can crawl")
class dog(animel):
    def move(self):
        print("I can bark")
class lion(animel):
    def move(self):
        print("I can hunt")
r=humen()
r.move()
r=snake()
r.move()
r=dog()
r.move()
r=lion()
r.move()