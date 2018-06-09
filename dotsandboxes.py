#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

XSLOT = 0
YSLOT = 0
CELL_SIZE = 70

def buildBoard():
    return [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]] 

def RedrawAll():
    data['x'] = 0
    data['y'] = 0
    blackOutline = LineStyle(5, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)
    for item in App().spritelist[:]:
        item.destroy()
    drawCenters()
    LeftEdges()
    RightEdges()
    UpperEdges()
    LowerEdges()
    data['x'] = data['x'] + 50
            
def LeftEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][0] == 0:
                blackOutline = LineStyle(8, black)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][0] == 1:
                redOutline = LineStyle(5, red)
                leftLine = Sprite(LineAsset(0,80, redOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][0]== 2:
                blueOutline = LineStyle(5, blue)
                leftLine = Sprite(LineAsset(0,80, blueOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
        data['x'] += 72
        data['y'] = 0


def UpperEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][1] == 0:
                blackOutline = LineStyle(8, black)
                leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 75
            elif board[i-1][j-1][1] == 1:
                redOutline = LineStyle(8, red)
                leftLine = Sprite(LineAsset(80,0, redOutline),((XSLOT-10)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 75
            elif board[i-1][j-1][1] == 2:   
                blueOutline = LineStyle(8, blue)
                leftLine = Sprite(LineAsset(80,0, blueOutline),((XSLOT-10)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 75
        data['x'] += 75
        data['y'] = 0

def RightEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][2] == 0:
                blackOutline = LineStyle(8, black)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT+55)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][2] == 1:
                redOutline = LineStyle(5, red)
                leftLine = Sprite(LineAsset(0,80, redOutline),((XSLOT+55)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][2] == 2:
                blueOutline = LineStyle(5, blue)
                leftLine = Sprite(LineAsset(0,80, blueOutline),((XSLOT+55)+data['x'], (YSLOT-5)+data['y']))
                data['y'] += 72
        data['x'] += 72
        data['y'] = 0
            
def LowerEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][3] == 0:
                blackOutline = LineStyle(8, black)
                leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT+60)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][3] == 1:
                redOutline = LineStyle(8, red)
                leftLine = Sprite(LineAsset(80,0, redOutline),((XSLOT-10)+data['x'], (YSLOT+60)+data['y']))
                data['y'] += 72
            elif board[i-1][j-1][3] == 2:
                blueOutline = LineStyle(8, blue)
                leftLine = Sprite(LineAsset(80,0, blueOutline),((XSLOT-10)+data['x'], (YSLOT+60)+data['y']))
                data['y'] += 72
        data['x'] += 75
        data['y'] = 0

def drawCenters():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][4] == 1:
                blackOutline = LineStyle(0, black)
                rectangleAsset = Sprite(RectangleAsset(60,60, blackOutline, red), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += 75
                data['playeronescore'] += 1
            elif board[i-1][j-1][4] == 2:
                blackOutline = LineStyle(0, black)
                rectangleAsset = Sprite(RectangleAsset(60,60, blackOutline, blue), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += 75
                data['playertwoscore'] += 1
            else:
                blackOutline = LineStyle(0, black)
                rectangleAsset = Sprite(RectangleAsset(60,60, blackOutline, gray), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += 75
        data['x'] += 75
        data['y'] = 0

def UpdateLeftEdges(a,b):
    if data['player'] == 1 and board[a][b][0] == 0:
        board[a][b][0] = 1
    elif data['player'] == 2 and board[a][b][0] == 0:
        board[a][b][0] = 2
def UpdateUpperEdges(a,b):
    if data['player'] == 1 and board[a][b][1] == 0:
        board[a][b][1] = 1
    elif data['player'] == 2 and board[a][b][1] == 0:
        board[a][b][1] = 2
def UpdateRightEdges(a,b):
    if data['player'] == 1 and board[a][b][2] == 0:
        board[a][b][2] = 1
    elif data['player'] == 2 and board[a][b][2] == 0:
        board[a][b][2] = 2
def UpdateLowerEdges(a,b):
    if data['player'] == 1 and board[a][b][3] == 0:
        board[a][b][3] = 1
    elif data['player'] == 2 and board[a][b][3] == 0:
        board[a][b][3] = 2
def UpdateCenters(a,b):
    if board[a][b][0] != 0 and board[a][b][1] != 0 and board[a][b][2] != 0 and board[a][b][3] != 0 and data['player'] == 1 and board[a][b][4] == 0:
        board[a][b][4] = 1
    elif board[a][b][0] != 0 and board[a][b][1] != 0 and board[a][b][2] != 0 and board[a][b][3] != 0 and data['player'] == 2 and board[a][b][4] == 0:
        board[a][b][4] = 2
        
def mouseClick(event):
    checkTurn()
    movex = event.x//CELL_SIZE
    movey = event.y//CELL_SIZE
    adjustx = event.x/CELL_SIZE
    adjusty = event.y/CELL_SIZE
    if abs(adjustx - movex) < 0.15 and abs(adjusty - movey) < 1:
        UpdateLeftEdges(movex, movey)
    if abs(adjustx - movex) < 0.15 and abs(adjusty - movey) < 0.5:
        UpdateRightEdges(movex-1, movey)
    if abs(adjustx - movex) <= 1 and abs(adjusty - movey) < 0.15:
        UpdateUpperEdges(movex, movey)
    if abs(adjustx - movex) < 0.5 and abs(adjusty - movey) < 0.15:
        UpdateLowerEdges(movex, movey-1) 
    UpdateCenters(movex, movey)
    RedrawAll()
    drawScore()
    print(board)
    
def drawScore():
    playeronetext = TextAsset(data['playeronescore'], fill = red, style = "bold 40pt Times")
    playertwotext = TextAsset(data['playertwoscore'], fill = blue, style = "bold 40pt Times")
    Sprite(playeronetext, (700, 100))
    Sprite(playertwotext, (700, 200))

def checkTurn():  
    data['totalturns'] += 1
    if data['totalturns']/2 == int(data['totalturns']/2):
        data['player'] = 2
    else:
        data['player'] = 1
    
board = buildBoard()

if __name__ == '__main__': 
    red = Color(0xFF0000, 1)
    blue = Color (0x0000FF, 1)
    gray = Color(0xD3D3D3, 1)
    black = Color (0x000000, 1)
    data = {}
    data['board'] = buildBoard()
    data['x'] = 0
    data['y'] = 0
    data['c'] = 0
    data['totalturns'] = 0
    data['player'] = 1
    data['playeronescore'] = 0
    data['playertwoscore'] = 0
    
    blackOutline = LineStyle(1, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)
    
    App().listenMouseEvent('click', mouseClick)
    App().run()
    RedrawAll()
    drawScore()
   
