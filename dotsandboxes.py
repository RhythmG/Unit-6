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
    for r in range(0,4):
            for c in range(0,2):
                pegs = EllipseAsset(10,50, blackOutline, black)
                data['x'] = data['x'] + 50
                """
                Sprite(vblackLine,(XSLOT + 50, YSLOT + data['y'])) #left edge
                Sprite(vblackLine,(XSLOT + 478, YSLOT + data['y'])) #right edge
                data['y'] = data['y'] + 50
                Sprite(hblackLine,(XSLOT + data['x'], YSLOT)) #top edge
                Sprite(hblackLine,(XSLOT + data['x'], YSLOT + 427)) #bottom edge
                """
            print()
            
def LeftEdge(startx, starty, currentx, currenty):
    data['x'] = 0
    data['y'] = 0
    c = 0
    for r in range(0,4):
        if data['board'][r][c] == 0:
            Sprite(vblackLine,(XSLOT + 50, YSLOT + data['y']))
            c = c+1

def RightEdge(startx, starty, currentx, currenty):
    XSLOT = 250
    data['x'] = 0
    data['y'] = 0
    c = 0
    for r in range(0,4):
        if data['board'][r][c] == 0:
            Sprite(vblackLine,(XSLOT + 478, YSLOT + data['y']))
            c = c+1

def UpperEdge(startx, starty, currentx, currenty):
    data['x'] = 0
    data['y'] = data['y'] + 50
    c = 0
    for r in range(0,4):
        if data['board'][r][c] == 0:
            Sprite(hblackLine,(XSLOT + data['x'], YSLOT))
            c = c+1
            
def LowerEdge(startx, starty, currentx, currenty):
    YSLOT = 130
    data['x'] = 0
    data['y'] = 0
    c = 0
    for r in range(0,4):
        if data['board'][r][c] == 0:
            Sprite(hblackLine,(XSLOT + data['x'], YSLOT + 427))
            c = c+1

board = buildBoard()

if __name__ == '__main__': 
    red = Color(0xFF0000, 1)
    blue = Color (0x0000FF, 1)
    black = Color (0x000000, 1)
    data = {}
    data['board'] = buildBoard()
    data['x'] = 0
    data['y'] = 0
    
    blackOutline = LineStyle(1, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)    
    
    
    App().run()
    RedrawAll()
    LeftEdge(XSLOT, YSLOT, data['x'], data['y'])
    RightEdge(XSLOT, YSLOT, data['x'], data['y'])
    
    
