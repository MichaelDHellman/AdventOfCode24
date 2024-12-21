if __name__ == "__main__":
    antDict = {}
    occList = []
    pinput = []
    with open("./day8.txt", 'r') as f:
        pinput = [i for i in f.read().split('\n')]
    for y in range(len(pinput)):
        for x in range(len(pinput[y])):
            if pinput[y][x] != '.':
                try:
                    antDict[pinput[y][x]].append((y,x))
                except KeyError as e:
                    antDict[pinput[y][x]] = [(y,x)]
    print(antDict)
    for freq in antDict:
        for origin in antDict[freq]:
            for target in antDict[freq]:
                if origin != target:
                    xdel = origin[0] - target[0]
                    ydel = origin[1] - target[1]
                    x = origin[0] + xdel
                    y = origin[1] + ydel
                    print("X: " + str(x) + " Y: " + str(y))
                    while x in range(0, len(pinput[0])) and y in range(0, len(pinput)): 
                        if (y,x) not in occList:
                            occList.append((y,x))
                        x += xdel
                        y += ydel
                    x = origin[0] - xdel
                    y = origin[1] - ydel
                    while x in range(0, len(pinput[0])) and y in range(0, len(pinput)): 
                        if (y,x) not in occList:
                            occList.append((y,x))
                        x -= xdel
                        y -= ydel
    print(len(occList))