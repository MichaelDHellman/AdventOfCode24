direction = {0: (1,1), 1: (1,0), 2: (1,-1), 3: (0,-1), 4: (-1,-1), 5: (-1,0), 6: (-1,1), 7:(0,1)}
found_positions = set()

def scan(y, x, world):
    count = 0
    for i in range(8):
        xdir = direction[i][0]
        ydir = direction[i][1]
        word = ""
        try:
            for j in range(4):
                if y+(ydir*j) < 0 or x+(xdir*j) < 0:
                    continue
                word += world[y+(ydir*j)][x+(xdir*j)]
            if word == "XMAS":
                count += 1
                
        except IndexError:
            pass
    return count

def mas_scan(world):
    if (len(world) < 3 or len(world[0]) < 3):
        return 0
    dir1 = world[0][0] + world[1][1] + world[2][2]
    dir2 = world[2][0] + world[1][1] + world[0][2]
    if (dir1 == "MAS" or dir1 == "SAM") and (dir2 == "MAS" or dir2 == "SAM"):
        return 1
    else:
        return 0
if __name__ == "__main__":
    pinput = ""
    count = 0
    count2 = 0
    with open("./day4.txt", 'r') as f:
        pinput = f.read()
    pinput = pinput.split('\n')
    for y in range(len(pinput)):
        for x in range(len(pinput[0])):
            if pinput[y][x] == 'X':
                count += scan(y,x,pinput)
            count2 += mas_scan([[j for j in i[x:x+3]] for i in pinput[y:y+3]])
    print(count)
    print(count2)