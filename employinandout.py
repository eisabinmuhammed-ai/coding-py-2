class Employ:
    def __init__(self):
        print("EMPLOY creted")
    def __del__(self):
        print("Desteracar called")
def creted_obj():
    print("Making object....")
    obj=Employ()
    print("funcsion end")
    return obj
print(creted_obj())