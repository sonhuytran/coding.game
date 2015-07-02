import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surfaceN = int(input()) # the number of points used to draw the surface of Mars.
for i in range(surfaceN):
    # landX: X coordinate of a surface point. (0 to 6999)
    # landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    landX, landY = [int(j) for j in input().split()]

# game loop
while 1:
    # hSpeed: the horizontal speed (in m/s), can be negative.
    # vSpeed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    X, Y, hSpeed, vSpeed, fuel, rotate, power = [int(i) for i in input().split()]
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    rotate_target = 0
    thrust_power = 4 if vSpeed <= -40 else 0
    
     # rotate power.
     # rotate is the desired rotation angle.
     # power is the desired thrust power.
    print(rotate_target, thrust_power)
