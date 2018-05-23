#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

XSLOT = 300
YSLOT = 100

red = Color(0xFF0000, 1)
blue = Color (0x0000FF, 1)
black = Color (0x000000, 1)

blackOutline = LineStyle(5, black)
vblackLine = LineAsset(0,80, blackOutline)
hblackLine = LineAsset(45, 0, blackOutline)

def buildBoard(a):
    for r in range(0,4):
        for c in range(0,4):
            print(board[r][c], end =' ')
        print()
    
row1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row3 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row4 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


board[row-1][col-1] = 1



App().run()

