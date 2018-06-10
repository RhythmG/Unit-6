#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

DIMENSION = 4
XSLOT = 0
YSLOT = 0
CELL_SIZE = 75
linethickness = 1
linesize = CELL_SIZE + linethickness

def buildBoard():
    return [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]] 
    
def RedrawAll():
    data['x'] = 0
    data['y'] = 0
    for item in App().spritelist[:]:
        item.destroy()
    drawCenters()
    LeftEdges()
    RightEdges()
    UpperEdges()
    LowerEdges()
    drawScore()
            
def LeftEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,DIMENSION + 1):
        for j in range(1,DIMENSION + 1):
            if board[i-1][j-1][0] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][0] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][0]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = 0

def UpperEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,DIMENSION + 1):
        for j in range(1,DIMENSION + 1):
            if board[i-1][j-1][1] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][1] == 1:
                leftLine = Sprite(LineAsset(linesize, 0, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][1]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
        data['y'] += CELL_SIZE + linethickness
        data['x'] = 0

def RightEdges():
    data['x'] = CELL_SIZE + linethickness
    data['y'] = 0
    for i in range(1,DIMENSION+1):
        for j in range(1,DIMENSION+1):
            if board[i-1][j-1][2] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][2] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][2]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = 0
            
def LowerEdges():
    data['x'] = 0
    data['y'] = CELL_SIZE + linethickness
    for i in range(1,DIMENSION+1):
        for j in range(1,DIMENSION+1):
            if board[i-1][j-1][3] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][3] == 1:
                leftLine = Sprite(LineAsset(linsize, 0, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][3]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['x'] += CELL_SIZE + linethickness
        data['y'] += CELL_SIZE + linethickness
        data['x'] = 0

def drawCenters():
    checkFace()
    data['x'] = linethickness
    data['y'] = linethickness
    for i in range(1,DIMENSION+1):
        for j in range(1,DIMENSION+1):
            if board[i-1][j-1][4] == 1:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], red), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i-1][j-1][4] == 2:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], blue), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            else:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], gray), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = linethickness
 

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

def mouseClick(event):
    checkTurn()
    movex = event.x//CELL_SIZE
    movey = event.y//CELL_SIZE
    adjustx = event.x/CELL_SIZE
    adjusty = event.y/CELL_SIZE
    if abs(adjustx - movex) < 0.15 and abs(adjusty - movey) < 1:
        UpdateLeftEdges(movex, movey)
    if abs(adjustx - movex) < 0.15 and abs(adjusty - movey) < 1 and movex != 0:
        UpdateRightEdges(movex-1, movey)
    if abs(adjustx - movex) <= 1 and abs(adjusty - movey) < 0.15:
        UpdateUpperEdges(movex, movey)
    if abs(adjustx - movex) < 0.5 and abs(adjusty - movey) < 0.15 and movey != 0:
        UpdateLowerEdges(movex, movey-1) 
    if movex == 3 and abs(adjustx - movex) < 0.75 and abs(adjusty-movey) < 0.4:
        UpdateRightEdges(movex, movey)
    if movey == 3 and abs(adjusty - movey) < 0.8 and abs(adjustx-movex) < 0.4:
        UpdateLowerEdges(movex, movey)
    RedrawAll()
    print(adjustx - movex)
    print(movex)
    print(adjusty - movey)
    print(board) 

def checkFace():
    for i in range(1,5):
        for j in range(1,5):
            if board[i-1][j-1][0] != 0 and board[i-1][j-1][1] != 0 and board[i-1][j-1][2] != 0 and board[i-1][j-1][3] != 0 and data['player'] == 1 and board[i-1][j-1][4] == 0:
                board[i-1][j-1][4] = 1
                data['playeronescore'] += 1
            elif board[i-1][j-1][0] != 0 and board[i-1][j-1][1] != 0 and board[i-1][j-1][2] != 0 and board[i-1][j-1][3] != 0 and data['player'] == 2 and board[i-1][j-1][4] == 0:
                board[i-1][j-1][4] = 2
                data['playertwoscore'] += 1
    
def drawScore():
    playeronetext = TextAsset("Player 1:", fill = red, style = "bold 18pt Times")
    playeronetext2 = TextAsset(data['playeronescore'], fill = red, style = "bold 40pt Times")
    playertwotext = TextAsset("Player 2:", fill = blue, style = "bold 18pt Times")
    playertwotext2 = TextAsset(data['playertwoscore'], fill = blue, style = "bold 40pt Times")
    Sprite(playeronetext, (580, 115))
    Sprite(playertwotext, (580, 215))
    Sprite(playeronetext2, (700, 100))
    Sprite(playertwotext2, (700, 200))

def checkTurn():  
    data['totalturns'] += 1
    if data['totalturns']/2 == int(data['totalturns']/2):
        data['player'] = 2
    else:
        data['player'] = 1
    print(data['totalturns'])
    
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
    data['noOutline'] = LineStyle(0, black)
    data['blackOutline'] = LineStyle(linethickness, black)
    data['redOutline'] = LineStyle(linethickness, red)
    data['blueOutline'] = LineStyle(linethickness, blue)
    data['totalturns'] = 0
    data['player'] = 1
    data['playeronescore'] = 0
    data['playertwoscore'] = 0
    
    App().listenMouseEvent('click', mouseClick)
    App().run()
    RedrawAll()
    