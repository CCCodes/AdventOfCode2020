inp_f = open("input/day10.txt", "r")
inp = inp_f.read()
inp_list = [int(line) for line in inp.split("\n") if line != ""]


def part1():
    prev = 0
    diff1 = 0
    diff3 = 1  # count last jump
    inp_list.sort()
    for num in inp_list:
        if num - prev == 1:
            diff1 += 1
        if num - prev == 3:
            diff3 += 1
        prev = num
    return diff1 * diff3


def part2():
    inp_list.sort()
    max_volts = inp_list[-1]
    # print(max_volts)
    idx = 0
    memo_table = [1]
    for i in range(1, max_volts+1):
        if i < inp_list[idx]:
            memo_table.append(0)
        else:
            memo_table.append(sum(memo_table[-3:]))
            idx += 1
    # print(memo_table)
    return memo_table[-1]


if __name__ == "__main__":
    # print(part1())
    print(part2())
