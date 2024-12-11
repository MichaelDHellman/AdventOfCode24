import copy

DIRECTION = {0: (-1,0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}

def movedir(ypos, xpos, dir, world, obstructionlist):
    while(world[ypos][xpos] != '#'):
        checkObsLoop(ypos,xpos,dir,world,obstructionlist)
        world[ypos][xpos] = 'X'
        xpos += DIRECTION[dir][0]
        ypos += DIRECTION[dir][1]
        if not ((xpos in range(len(world[0]))) and (ypos in range(len(world)))):
            return 5, ypos, xpos
    return ((dir+1) % 4), ypos - DIRECTION[dir][1], xpos - DIRECTION[dir][0]
    
def checkObsLoop(ypos,xpos,dir,world,obstructionlist):
    if (ypos + DIRECTION[dir][1]) in range(len(world)) and (xpos + DIRECTION[dir][0]) in range(len(world[0])):
        newworld = copy.deepcopy(world)
        newworld[ypos + DIRECTION[dir][1]][xpos + DIRECTION[dir][0]] = '#'
        visited = [(ypos + DIRECTION[dir][1], xpos + DIRECTION[dir][0],5)]
        while(dir != 5):
            dir, ypos, xpos = drymove(ypos, xpos, dir, newworld, obstructionlist, visited)


def drymove(ypos, xpos, dir, world, obstructionlist, visited):
    while(world[ypos][xpos] != '#'):
        xpos += DIRECTION[dir][0]
        ypos += DIRECTION[dir][1]
        if not ((xpos in range(len(world[0]))) and (ypos in range(len(world)))):
            return 5, ypos, xpos
    if visited.count((ypos,xpos, dir)) > 2:
        if ((visited[0][1],visited[0][0])) not in obstructionlist:
            obstructionlist.append(((visited[0][1],visited[0][0])))
        return 5, ypos, xpos
    visited.append((ypos,xpos,dir))
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
    obstructionlist = []
    dir = 1
    while(dir != 5):
        dir, y, x = movedir(y, x, dir, pinput, obstructionlist)
    print(sum([i.count('X') for i in pinput]))
    print(obstructionlist)
    print(len(set(obstructionlist)))