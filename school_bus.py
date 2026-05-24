class vecel:
    def __init__(self,name,speed,mileg):
        self.speed=speed
        self.mileg=mileg
        self.name=name
class bus(vecel):
    pass
school_bus=bus("school volvo",240,12)
print("the name of the the school bus is",school_bus.name,"the speed of the bus is ",school_bus.speed,"the mieg of the bus is ",school_bus.mileg)