class gameBoard:
    def __init__(self):
        self.board = 10*[10*[0]]
        self.Iboard = self.getBoard(self.board)

    def getBoard(self, setboard):
        setboard[0][0] = "a"
        setboard[0][1] = "b"
        setboard[0][2] = "c"
        setboard[0][3] = "d"
        setboard[0][4] = "e"
        setboard[0][5] = "f"
        setboard[0][6] = "g"
        setboard[0][7] = "h"
        setboard[0][8] = "i"
        setboard[0][9] = "j"
        return setboard
            
