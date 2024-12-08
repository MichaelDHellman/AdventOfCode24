def strictdiff(inp):
    for i in range(len(inp) - 1):
        dff = inp[i+1] - inp[i]
        if (inp[1] - inp[0]) * dff < 0:
            return False
        elif dff == 0:
            return False 
        elif not (abs(dff) >= 1 and abs(dff) <= 3):
            return False
    return True

def diff(inp):
    for i in range(len(inp)):
        if (strictdiff(inp[0:i] + inp[i+1:])):
            return 1
    return 0

if __name__ == "__main__":
    pinput = []
    with open("./day2.txt", 'r') as f:
        pinput = [[int(x) for x in i.split(' ')] for i in f.read().split('\n')]
    print(pinput)
    good = sum([diff(i) for i in pinput])
    print(good)
    print(diff([7,6,4,2,1]))