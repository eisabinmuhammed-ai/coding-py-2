class bird:
    def __init__(self):
        print("bird is ready")
    def whoisit(self):
        print("bird")
    def swim(self):
        print("swim faster")
class pengen(bird):
    def __init__(self):
        super().__init__()
        print("pengen is ready")
    def whoisit(self):
        print("pengen")
    def run(self):
        print("run faster")
peggey=pengen()
peggey.whoisit()
peggey.swim()
peggey.run()