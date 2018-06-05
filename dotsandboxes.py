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
        for i in range(1,5):
            if board[0][i-1] == 0:
                blackOutline = LineStyle(5, black)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['x'] += 80
            elif board[0][i-1] == 1:
                blackOutline = LineStyle(5, red)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['x'] += 80
            elif board[0][i-1] == 2:
                blackOutline = LineStyle(5, blue)
                leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT-5)+data['x'], (YSLOT-5)+data['y']))
                data['x'] += 80
        data['y'] += 80
        data['x'] = 0

def RightEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(5, black)
            leftLine = Sprite(LineAsset(0,80, blackOutline),((XSLOT+55)+data['x'], (YSLOT-5)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0

def UpperEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(5, black)
            leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT-5)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0
            
def LowerEdges():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            blackOutline = LineStyle(5, black)
            leftLine = Sprite(LineAsset(80,0, blackOutline),((XSLOT-10)+data['x'], (YSLOT+60)+data['y']))
            data['x'] += 80
        data['y'] += 80
        data['x'] = 0

def drawCenters():
    data['x'] = 0
    data['y'] = 0
    for i in range(1,5):
        for i in range(1,5):
            rectangleAsset = Sprite(RectangleAsset(60,60, blackOutline, gray), (XSLOT+data['x'], YSLOT+data['y']))
            data['x'] = data['x'] + 80
        data['y'] = data['y'] + 80
        data['x'] = 0

"""        
def mouseClick(event):
    if event.x <= 200 and event.y >= 80:
        for i in range(1, 5):
            if buildBoard == 0:
                
    if event.x >= 200 and event.y <= 80:
        for i in range(1, 5):
            if buildBoard([1][i])
    if event.x <= 200 and event.y >= 80:
        for i in range(1, 5):
            if buildBoard([2][i]) == 0:
    if event.x >= 480 and event.y >= 80:
        for i in range(1, 5):
            if buildBoard([3][i])
    if event.x >= 480 and event.y >= 560:
        for i in range(1, 5):
            if buildBoard([4][i])
"""
    

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
    data['player'] = 1
    
    blackOutline = LineStyle(1, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)
    
    """
    App().listenMouseEvent('click', mouseClick)
    """
    App().run()
    RedrawAll()
   
    
    

    
    
    

    
