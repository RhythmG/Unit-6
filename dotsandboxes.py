#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

DIMENSION = 4
XSLOT = 50
YSLOT = 53
CELL_SIZE = 75
linethickness = 1
linesize = CELL_SIZE + linethickness
tolerance = 0.1

def buildBoard():
    return [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]] 

def RedrawAll():
    data['x'] = XSLOT
    data['y'] = YSLOT
    for item in App().spritelist[:]:
        item.destroy()
    drawCenters()
    LeftEdges()
    RightEdges()
    UpperEdges()
    LowerEdges()
    drawScore()
            
def LeftEdges():
    data['x'] = XSLOT
    data['y'] = YSLOT
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][0] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(data['x'], data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][0] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][0]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = YSLOT

def UpperEdges():
    data['x'] = XSLOT
    data['y'] = YSLOT
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][1] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][1] == 1:
                leftLine = Sprite(LineAsset(linesize, 0, data['redOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][1]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = YSLOT

def RightEdges():
    data['x'] = XSLOT+ CELL_SIZE + linethickness
    data['y'] = YSLOT
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][2] == 0:
                leftLine = Sprite(LineAsset(0,linesize, data['blackOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][2] == 1:
                leftLine = Sprite(LineAsset(0,linesize, data['redOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][2]== 2:
                leftLine = Sprite(LineAsset(0,linesize, data['blueOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = YSLOT
            
def LowerEdges():
    data['x'] = XSLOT
    data['y'] = YSLOT + CELL_SIZE + linethickness
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][3] == 0:
                leftLine = Sprite(LineAsset(linesize,0, data['blackOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][3] == 1:
                leftLine = Sprite(LineAsset(linesize, 0, data['redOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][3]== 2:
                leftLine = Sprite(LineAsset(linesize, 0, data['blueOutline']),(data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] =  YSLOT + CELL_SIZE + linethickness

def drawCenters():
    data['x'] = XSLOT + linethickness
    data['y'] = YSLOT + linethickness
    for i in range(0,DIMENSION):
        for j in range(0,DIMENSION):
            if board[i][j][4] == 1:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], lightred), (data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            elif board[i][j][4] == 2:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], lightblue), (data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
            else:
                rectangleAsset = Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE, data['noOutline'], gray), (data['x'],data['y']))
                data['y'] += CELL_SIZE + linethickness
        data['x'] += CELL_SIZE + linethickness
        data['y'] = YSLOT + linethickness
 

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
        
def GameFinish(ascore, bscore):
    if ascore + bscore == 16:
        if ascore > bscore:
            print('Player 1 Wins!')
            return True
        elif ascore < bscore:
            print('Player 2 Wins!')
            return True
        else:
            print('Tie Game!')
            return True
    else:
        return False

def mouseClick(event):
    if GameFinish(data['playeronescore'], data['playertwoscore']):
        return
    checkTurn()
    adjustx = (event.x-XSLOT)/(CELL_SIZE+linethickness)
    adjusty = (event.y-YSLOT)/(CELL_SIZE+linethickness)
    roundx = round(adjustx, 0)
    roundy = round(adjusty, 0) 
    floorx = (event.x-XSLOT)//(CELL_SIZE+linethickness)
    floory = (event.y-YSLOT)//(CELL_SIZE+linethickness)
    
    if roundx > DIMENSION or roundy > DIMENSION:
        print("Out of board")
        return 
    if abs(adjustx - roundx) < tolerance:
        turnForward = False
        if roundx < DIMENSION:
            UpdateLeftEdges(roundx, floory)
            turnFace = checkFace(roundx,floory)
            if turnFace:
                turnForward = True
            if roundx > 0:
                UpdateRightEdges(roundx-1, floory)
                turnFace = checkFace(roundx-1,floory)
                if turnFace:
                    turnForward = True
        else:
            UpdateRightEdges(roundx-1, floory)
            turnFace = checkFace(roundx-1,floory)
            if turnFace:
                    turnForward = True
        if turnForward:
            data['totalturns'] += 1
    elif abs(adjusty - roundy) < tolerance:
        turnForward = False
        if roundy < DIMENSION:
            UpdateUpperEdges(floorx, roundy)
            turnFace = checkFace(floorx,roundy)
            if turnFace:
                    turnForward = True
            if roundy > 0:
                UpdateLowerEdges(floorx, roundy-1)
                turnFace = checkFace(floorx,roundy-1)
                if turnFace:
                    turnForward = True
        else:
            UpdateLowerEdges(floorx, roundy-1)
            turnFace = checkFace(floorx,roundy-1)
            if turnFace:
                    turnForward = True
        if turnForward:
            data['totalturns'] += 1           
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
        if data['player'] == 1:
            board[id][jd][4] = 1
            data['playeronescore'] += 1
            GameFinish(data['playeronescore'], data['playertwoscore'])
        else:
            board[id][jd][4] = 2
            data['playertwoscore'] += 1
            GameFinish(data['playeronescore'], data['playertwoscore'])
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
