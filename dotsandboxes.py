#Stephen Wang
#5/23/18
#Final project - Dots and boxes

from ggame import *

XSLOT = 200
YSLOT = 80



def buildBoard():
    return [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]] 

"""
pegs = EllipseAsset(10,50, blackOutline, black)
"""

def RedrawAll():
    x = 0
    y = 0
    blackOutline = LineStyle(5, black)
    vblackLine = LineAsset(0,80, blackOutline)
    hblackLine = LineAsset(80, 0, blackOutline)
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(0,4):
            for c in range(0,2):
                x = x + 50
                Sprite(vblackLine,(XSLOT + 50, YSLOT + y)) #left edge
                Sprite(vblackLine,(XSLOT + 478, YSLOT + y)) #right edge
                y = y + 50
                Sprite(hblackLine,(XSLOT + x, YSLOT)) #top edge
                Sprite(hblackLine,(XSLOT + x, YSLOT + 427)) #bottom edge
            print()
            
"""
def LeftEdge(a, b, c, d):

"""
       

if __name__ == '__main__': 
    red = Color(0xFF0000, 1)
    blue = Color (0x0000FF, 1)
    black = Color (0x000000, 1)
    data = {}
    data['board'] = buildBoard()
    
    
    
    App().run()
    RedrawAll()
    """
    LeftEdge(XSLOT, YSLOT, x, y)
    """
    
    
