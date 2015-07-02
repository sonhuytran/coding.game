import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

fired = False
def debug(*args):
    print(*args, file=sys.stderr)

# game loop
while 1:
    spaceX, spaceY = [int(i) for i in input().split()]
    maxH, maxCell = -1, -1
    
    if spaceX == 0 or spaceX == 7:
        # We can fire for each pass
        fired = False
    
    for i in range(8):
        # represents the height of one mountain, from 9 to 0.
        # Mountain heights are provided from left to right.
        height = int(input())
        
        # Find the position of the highest mountain
        if height > maxH:
            maxH = height
            maxCell = i
            
    debug(maxH, maxCell, spaceX, spaceY, fired)
                
    if spaceX == maxCell and not fired:
        print("FIRE")
        fired = True
    else:
        print("HOLD")
    
    # Write an action using print
    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    # To debug: print("Debug messages...", file=sys.stderr)
