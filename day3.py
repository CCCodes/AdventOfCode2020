inp_f = open("input/day3.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1(right_inc, down_two=False):
    pos = 0
    size = len(inp_list[0])
    trees = 0
    for i, line in enumerate(inp_list):
        if down_two and i % 2 == 1:
            continue
        if line[pos % size] == "#":
            trees += 1
        pos += right_inc
    return trees


def part2():
    acc = 1
    for i in range(1, 8, 2):
        acc *= part1(i)
    acc *= part1(1, True)
    return acc


if __name__ == "__main__":
    print(part2())