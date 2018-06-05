#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

XSLOT = 200
YSLOT = 80

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
    pegs = EllipseAsset(10,50, blackOutline, black)
    data['x'] = data['x'] + 50
    """
    Sprite(vblackLine,(XSLOT + 50, YSLOT + data['y'])) #left edge
    Sprite(vblackLine,(XSLOT + 478, YSLOT + data['y'])) #right edge
    data['y'] = data['y'] + 50
    Sprite(hblackLine,(XSLOT + data['x'], YSLOT)) #top edge
    Sprite(hblackLine,(XSLOT + data['x'], YSLOT + 427)) #bottom edge
    """
            
def LeftEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for j in range(1,5):
            if board[0][i-1][j-1] == 0:
                blackOutline = LineStyle(8, black)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['x'] += 80
            elif board[0][i-1][j-1] == 1 and data['player'] == 1:
                
                data['x'] += 80
            elif board[0][i-1][j-1] == 2 and data['player'] == 2:
                blueOutline = LineStyle(5, blue)
                leftLine = Sprite(LineAsset(0,80, blueOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['x'] += 80
        data['y'] += 80
        data['x'] = 0

def RightEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(8, black)
            leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT+55)+data['x'], (YSLOT-5)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0

def UpperEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(8, black)
            leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT-5)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0
            
def LowerEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(8, black)
            leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT+60)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0
        
def UpdateLeftEdges(a,b):
    if data['player'] == 1:
        redOutline = LineStyle(5, red)
        leftLine = Sprite(LineAsset(0,80, redOutline),(a,b))
    elif data['player'] == 2:
        blueOutline = LineStyle(5, blue)
        leftLine = Sprite(LineAsset(0,80, blueOutline),(a,b))
    

def drawCenters():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            rectangleAsset = Sprite(RectangleAsset(60,60, blackOutline, gray), (XSLOT+data['x'], YSLOT+data['y']))
            data['x'] = data['x'] + 80
        data['y'] = data['y'] + 80
        data['x'] = 0

def mouseClick(event):
    if event.x <= XSLOT and event.y >= YSLOT:
        checkTurn()
        for i in range(1, 5):
            if board[0][i-1][0] == 0:
                UpdateLeftEdges(event.x, event.y)
            else:
                print("This line is already taken.")
                break
    elif event.x >= XSLOT and event.y <= YSLOT:
        checkTurn()
        for i in range(1, 5):
            if board[1][i-1][1] == 0:
                UpperEdges()
            else:
                print("This line is already taken.")
                break
    elif event.x <= XSLOT and event.y >= 80:
        checkTurn()
        for i in range(1, 5):
            for j in range(1,5):
                if board[2][i-1][2] == 0:
                    RightEdges()
            else:
                print("This line is already taken.")
                break
    elif event.x >= 480 and event.y >= YSLOT:
        checkTurn()
        for i in range(1, 5):
            if board[3][i-1][3] == 0:
                LowerEdges()
            else:
                print("This line is already taken.")
                break
    
def checkTurn():  
    data['totalturns'] += 1
    if data['totalturns']/2 == 0:
        data['player'] = 2
    elif data['totalturns'] == 0.5:
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
    data['totalturns'] = 0
    data['player'] = 1
    
    blackOutline = LineStyle(1, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)
    
    App().listenMouseEvent('click', mouseClick)
    App().run()
    RedrawAll()
   
    
    

    
    
    

    
