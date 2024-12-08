if __name__ == "__main__":
    #Part 1
    input = ""
    with open('./day1.txt', 'r') as f:
        input = f.read()
    inlines = filter(lambda a: a != '', input.split('\n'))
    inlines = [[int(x) for x in i.split('   ') if len(i.split('   ')) > 1] for i in inlines]
    print(inlines)
    xlist = sorted([i[0] for i in inlines])
    ylist = sorted([i[1] for i in inlines])
    print()
    total = 0
    for i in range(len(inlines)):
        total += abs(xlist[i] - ylist[i])
    print(total)
    #Part 2
    hashtable = {}
    for x in xlist:
        hashtable[x] = 0
    for y in ylist:
        try:
            hashtable[y] += 1
        except KeyError as e:
            pass
    total = 0
    for i in hashtable:
        total += hashtable[i] * i
    print(total)