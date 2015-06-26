import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor does not follow your orders.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# initialTX: Thor's starting X position
# initialTY: Thor's starting Y position
LX, LY, x, y = [int(i) for i in input().split()]
N, E, S, W = "N", "E", "S", "W"

# game loop
while True:
    # The level of Thor's remaining energy,
    # representing the number of moves he can still make.
    energy = int(input()) 
    
    # Write an action using print
    # print("energy =", energy, file=sys.stderr)
    moveX, moveY = "", ""
    dx, dy = 0, 0
    
    if x > LX:
        moveX = W
        dx = -1
    elif x < LX:
        moveX = E
        dx = 1
    
    if y > LY:
        moveY += N
        dy = -1
    elif y < LY:
        moveY += S
        dy = 1
    # A single line providing the move to be made:
    # N NE E SE S SW W or NW
    print(moveY + moveX)
    x += dx
    y += dy
