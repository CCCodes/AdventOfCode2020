import numpy as np

inp_f = open("input/test.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    mem = {}
    mask = [None, None]
    for line in inp_list:
        assign = line.split(" = ")
        if assign[0] == "mask":
            str_mask = assign[1]
            mask[0] = int(str_mask.replace("X", "1"), 2)
            mask[1] = int(str_mask.replace("X", "0"), 2)
        else:
            key = assign[0].split("[")[1][:-1]
            old_val = int(assign[1]) 
            mem[key] = old_val & mask[0] | mask[1]
    return sum(mem.values())


def part2():
    mem = {}
    mask = [None, None, None]
    for line in inp_list:
        assign = line.split(" = ")
        if assign[0] == "mask":
            str_mask = assign[1]
            # mask to turn X's -> 0's
            step1 = str_mask.replace("0", "1")
            mask[0] = int(step1.replace("X", "0"), 2)

            # 1's mask
            mask[1] = int(str_mask.replace("X", "0"), 2)

            # X positions
            idxs = list(np.where(np.array(list(str_mask)) == "X")[0])
            mask[2] = [35 - idx for idx in idxs]

        else:
            key = int(assign[0].split("[")[1][:-1])
            key = key & mask[0]
            key = key | mask[1]
            to_add = [0]
            for idx in mask[2]:
                to_add += [2 ** idx + e for e in to_add]
            val = int(assign[1]) 
            for add in to_add:
                mem[key+add] = val
    return sum(mem.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
