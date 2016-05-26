import player
import gameboard

def gameMenu():
    print("[1]Single player\n[2]Multiplayer")
    gamechoice = int(input("Choose your gametype: "))

    if gamechoice == 1:
        print("singleplayer")
        singlePlayer()
    elif gamechoice == 2:
        print("multiplayer")
        multiPlayer()
    return

def singlePlayer():
    _boardClass = gameboard.gameBoard()
    for x in range(0, 10):
        print(str(x), end="  ")
        for y in range(0, 10):
            print(_boardClass.Iboard[x][y], end=" ")
        print("")    
    return
            
   
        
    
def multiPlayer():

    return
