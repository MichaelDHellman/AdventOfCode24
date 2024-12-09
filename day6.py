DIRECTION = {0: (-1,0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}

def movedir(ypos, xpos, dir, world):
    while(world[ypos][xpos] != '#'):
        world[ypos][xpos] = "X"
        xpos += DIRECTION[dir][0]
        ypos += DIRECTION[dir][1]
        if not ((xpos in range(len(world[0]))) and (ypos in range(len(world)))):
            return 5, ypos, xpos
    return ((dir+1) % 4), ypos - DIRECTION[dir][1], xpos - DIRECTION[dir][0]

def getStart(world):
    for i in range(len(world)):
        if '^' in world[i]:
            return i, world[i].index('^')

if __name__ == "__main__":
    pinput = ""
    with open("./day6.txt", 'r') as f:
        pinput = [list(i) for i in f.read().split('\n')]
    y, x = getStart(pinput)
    dir = 1
    while(dir != 5):
        dir, y, x = movedir(y, x, dir, pinput)
    print(sum([i.count('X') for i in pinput]))
    