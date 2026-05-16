thebord={7:" ",8:" ",9:" "
        ,4:" ",5:" ",6:" ",
         1:" ",2:" ",3:" "}
bordkeys=[]
for key in thebord:
    bordkeys.append(key)
def printbord(bord):
    print(bord[7]+"|"+bord[8]+"|"+bord[9])
    print("-+-+-")
    print(bord[4]+"|"+bord[5]+"|"+bord[6])
    print("-+-+-")
    print(bord[1]+"|"+bord[2]+"|"+bord[3])
def game():
    turn="x"
    cont=0
    for i in range(10):
        printbord(thebord)
        move=input()
        if thebord[move]==" ":
            thebord[move]=turn
            cont=cont+1
        else:
            print("the place is already tooken \n where do you whant to put")
            continue
        if cont >= 5:
            if thebord[7]==thebord[8]==thebord[9]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[4]==thebord[5]==thebord[6]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[1]==thebord[2]==thebord[3]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[1]==thebord[4]==thebord[7]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[2]==thebord[5]==thebord[8]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[3]==thebord[6]==thebord[9]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[7]==thebord[5]==thebord[3]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
            elif thebord[1]==thebord[5]==thebord[9]:
                printbord(thebord)
                print("game over")
                print(turn," won")
                break
        if cont==9:
            print("game over \n its a tie")
        if turn=="x":
            turn="0"
        else:
            turn="x"
    restaret=input("do you whant to play again: ")
    if restaret == "y" or "yes":
        for key in bordkeys:
            thebord[key]=" "
        game()
if __name__=="__main__":
    game()