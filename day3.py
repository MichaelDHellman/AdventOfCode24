import re
if __name__ == "__main__":
    pinput = []
    with open("./day3.txt", 'r') as f:
        pinput = f.read()
    print(len(pinput))
    start = 0
    dontflag = False

    while True:
        dont_match = re.search("don't\(\)", pinput[start:])
        do_match = re.search("do\(\)", pinput[start:])

        if dont_match is None and do_match is None:
            break

        if do_match is not None and (dont_match is None or do_match.start() < dont_match.start()):
            if dontflag:
                pinput = pinput[:start] + pinput[do_match.start() + start + len("do"):] 
                start += 1
            else:
                start = do_match.start() + start + len("do()") + 1
            dontflag = False
        else:
            if dontflag:
                pinput = pinput[:start] + pinput[dont_match.start() + start + len("don't()"):] 
                start += 1
            else:
                start = dont_match.start() + start + len("don't()") + 1
            dontflag = True

        
    matches = re.findall("mul\((\d+),(\d+)\)", pinput)
    print(matches)
    tot = 0
    for m in matches:
        tot += int(m[0]) * int(m[1])
    print(tot)