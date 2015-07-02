import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def debug(*args):
    print(*args, file=sys.stderr)

road = int(input()) # the length of the road before the gap.
gap = int(input()) # the length of the gap.
platform = int(input()) # the length of the landing platform.
jumped = False

debug(road, gap, platform)

# game loop
while 1:
    speed = int(input()) # the motorbike's speed.
    coordX = int(input()) # the position on the road of the motorbike.
    
    debug(speed, coordX)
    
    # Write an action using print
    if jumped:
        print("SLOW" if speed > 0 else "WAIT")
    else:
        if coordX == road - 1:
            print("JUMP")
            jumped = True
        elif speed == gap + 1:
            print("WAIT")
        else:
            print("SPEED" if speed <= gap else "SLOW")
