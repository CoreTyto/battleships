import game

print("Welcome to STIL gaming's BATTLESHIPS!")
print("[1] New Game\n[Q]Exit")
menuchoice = input("Choice: ")         
if menuchoice == "1":
    print("new game")
    game.gameMenu()
elif menuchoice == "Q":
    print("Exiting game")
