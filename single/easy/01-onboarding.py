import sys, math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.


# game loop
while True:
    [enemy1, dist1, enemy2, dist2] \
        = [input() for _ in range(4)]
    dist1 = int(dist1)
    dist2 = int(dist2)
    
    enemy = enemy1 if dist1 < dist2 else enemy2
    print(enemy)
