inp_f = open("input/day8.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    idx = 0
    lines = []
    acc = 0
    while True:
        if idx in lines:
            return acc
        line = inp_list[idx]
        lines.append(idx)
        instr = line.split(" ")
        if instr[0] == "nop":
            idx += 1
        elif instr[0] == "acc":
            change = int(instr[1][1:])
            if instr[1][0] == "+":
                acc += change
            else:
                acc -= change
            idx += 1
        elif instr[0] == "jmp":
            change = int(instr[1][1:])
            if instr[1][0] == "+":
                idx += change
            else:
                idx -= change
    return -1


def tryIt(inps):
    idx = 0
    lines = []
    acc = 0
    while True:
        if idx in lines:
            return -1  # infinite loop
        if idx == len(inps):
            return acc
        line = inps[idx]
        lines.append(idx)
        instr = line.split(" ")
        if instr[0] == "nop":
            idx += 1
        elif instr[0] == "acc":
            change = int(instr[1][1:])
            if instr[1][0] == "+":
                acc += change
            else:
                acc -= change
            idx += 1
        elif instr[0] == "jmp":
            change = int(instr[1][1:])
            if instr[1][0] == "+":
                idx += change
            else:
                idx -= change
    return -1

def part2():
    for i, line in enumerate(inp_list):
        instr = line.split(" ")[0]
        if instr == "acc":
            continue
        val = line.split(" ")[1]
        inps = inp_list.copy()
        if instr == "nop":
            inps[i] = "jmp " + val
            trying = tryIt(inps)
            if trying != -1:
                return trying
        if instr == "jmp":
            inps[i] = "nop " + val
            trying = tryIt(inps)
            if trying != -1:
                return trying


if __name__ == "__main__":
    print(part2())
