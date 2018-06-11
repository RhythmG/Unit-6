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
tolerance = 0.1

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
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][0] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][0] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][0]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = 0

def UpperEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][1] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][1] == 1:
                leftLine = Sprite(LineAsset(linesize, 0, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][1]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = 0

def RightEdges():
    data['x'] = CELL_SIZE + linethickness
    data['y'] = 0
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][2] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][2] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][2]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = 0
            
def LowerEdges():
    data['x'] = 0
    data['y'] = CELL_SIZE + linethickness
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][3] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][3] == 1:
                leftLine = Sprite(LineAsset(linesize, 0, data['redOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][3]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] =  CELL_SIZE + linethickness

def drawCenters():
    data['x'] = linethickness
    data['y'] = linethickness
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][4] == 1:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], lightred), (XSLOT+data['x'], YSLOT+data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][4] == 2:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], lightblue), (XSLOT+data['x'], YSLOT+data['y']))
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
    adjustx = event.x/(CELL_SIZE+linethickness)
    adjusty = event.y/(CELL_SIZE+linethickness)
    roundx = round(adjustx, 0)
    roundy = round(adjusty, 0) 
    floorx = event.x//(CELL_SIZE+linethickness)
    floory = event.y//(CELL_SIZE+linethickness)
    
    if roundx > DIMENSION or roundy > DIMENSION:
        print("Out of board")
        return 
    if abs(adjustx - roundx) < tolerance:
        if roundx < DIMENSION:
            UpdateLeftEdges(roundx, floory)
            turnFace = checkFace(roundx,floory)
            if roundx > 0:
                UpdateRightEdges(roundx-1, floory)
                turnFace = checkFace(roundx-1,floory)
        else:
            UpdateRightEdges(roundx-1, floory)
            turnFace = checkFace(roundx-1,floory)
    elif abs(adjusty - roundy) < tolerance:
        if roundy < DIMENSION:
            UpdateUpperEdges(floorx, roundy)
            turnFace = checkFace(floorx,roundy)
            if roundy > 0:
                UpdateLowerEdges(floorx, roundy-1)
                turnFace = checkFace(floorx,roundy-1)
        else:
            UpdateLowerEdges(floorx, roundy-1)
            turnFace = checkFace(floorx,roundy-1)
    RedrawAll()

def checkFace(id,jd):
    if id > DIMENSION-1 or jd > DIMENSION-1:
        print ("face index out of range")
        return False
    turnface = True
    for k in range(0, 4):
        if board[id][jd][k] == 0:
            turnface = False
            break
    if turnface == True:
        data['totalturns'] += 1
        """if data['playeronescore'] + data['playertwoscore'] >= 16 and data['playeronescore'] > data['playertwoscore']:
            playeronewins = TextAsset("Player 1 Wins!", fill = red, style = "bold 18pt Times")
            Sprite(playeronewins, (400, 300))
        elif data['playeronescore'] + data['playertwoscore'] >= 16 and data['playertwoscore'] > data['playeronescore']:
            playertwowins = TextAsset("Player 2 Wins!", fill = blue, style = "bold 18pt Times")
            Sprite(playeronewins, (500, 300)) """
        if data['player'] == 1:
            board[id][jd][4] = 1
            data['playeronescore'] += 1
        else:
            board[id][jd][4] = 2
            data['playertwoscore'] += 1
    return turnface
    
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
    
board = buildBoard()

if __name__ == '__main__': 
    red = Color(0xFF0000, 1)
    lightred = Color(0xF08080, 1)
    blue = Color(0x0000FF, 1)
    lightblue = Color(0xA6CCFF, 1)
    gray = Color(0xD3D3D3, 1)
    black = Color (0x000000, 1)
    data = {}
    data['board'] = buildBoard()
    data['x'] = 0
    data['y'] = 0
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
