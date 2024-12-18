def parse_input_line(input_line):
    parts = input_line.split(": ")
    first_number = int(parts[0])
    number_list = [int(num) for num in parts[1].strip().split()]
    return first_number, number_list

def check_formable(goal, vals):
    for i in range(2**(len(vals)-1)):
        val = vals[0]
        bStr = format(i, 'b')
        bStr = bStr.rjust(len(format((2**(len(vals)-1))-1, 'b')), '0')
        for j,b in enumerate(bStr):
            if b == '0':
                val = val + vals[j+1]
            else:
                val = val * vals[j+1]
        if val == goal:
            return val
    return 0

def check_formable_p2(goal, vals):
    for i in range(3**(len(vals)-1)):
        val = vals[0]
        bStr = ternary_format(i)
        bStr = bStr.rjust(len(ternary_format((3**(len(vals)-1))-1)), '0')
        for j,b in enumerate(bStr):
            if b == '0':
                val = val + vals[j+1]
            elif b == '1':
                val = val * vals[j+1]
            elif b == '2':
                val = int(str(val) + str(vals[j+1]))
        if val == goal:
            return val
    return 0

def ternary_format(num):
    outstr = ''
    while(num > 0):
        outstr = str(num % 3) + outstr
        num //= 3
    return outstr

if __name__ == "__main__":
    pinput = ""
    with open("./day7.txt", 'r') as f:
        pinput = [i for i in f.read().split('\n')]
    pinput = [parse_input_line(i) for i in pinput]
    print(max([len(i[1]) for i in pinput]))
    outcomes = [check_formable(i,j) for i,j in pinput]
    print(sum(outcomes))
    outcomesP2 = [check_formable_p2(i,j) for i,j in pinput]
    print(sum(outcomesP2))