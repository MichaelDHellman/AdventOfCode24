from dataclasses import dataclass
    
if __name__ == "__main__":
    total = 0
    pageset = set()
    pagelist = {}
    pinput = ""
    with open("./day5.txt", 'r') as f:
        pinput = f.read()
    pinput = pinput.split('\n')
    for l in range(len(pinput)):
        if '|' in pinput[l]:
            pre, req = pinput[l].split('|')
            try:
                pagelist[int(req)].append(int(pre))
            except KeyError as e:
                pagelist[int(req)] = [int(pre)]
            pageset.add(int(req))
            pageset.add(int(pre))
        else:
            pinput = pinput[l+1:]
            break
    tofix = []
    for update in pinput:
        pages = [int(i) for i in update.split(',')]
        pageset.update(pages)
        flag = True
        filledset = pageset - set(pages)
        for p in pages:
            try:
                if not set(pagelist[p]).issubset(filledset):
                    flag = False
                    break
            except KeyError as e:
                pass
            filledset.add(p)
        if flag:
            total += pages[len(pages)//2]
        else:
            tofix.append(update)
    fixed = []
    for update in tofix:
        corder = []
        pages = [int(i) for i in update.split(',')]
        pageset.update(pages)
        filledset = pageset - set(pages)
        while(len(pages)) > 0:
            try:
                if not set(pagelist[pages[0]]).issubset(filledset):
                    pages.append(pages.pop(0))
                else:
                    corder.append(pages[0])
                    filledset.add(pages[0])
                    pages.pop(0)
            except KeyError as e:
                corder.append(pages[0])
                filledset.add(pages[0])
                pages.pop(0)
        fixed.append(corder)
    total2=0
    total2 += sum([i[len(i)//2] for i in fixed])
    print(total)
    print(total2)
    