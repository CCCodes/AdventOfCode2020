inp_f = open("input/day6.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n\n") if line != ""]


def part1():
    sum = 0
    for group in inp_list:
        splitted = [list(ans) for ans in group.split("\n")]
        one_list = [i for j in splitted for i in j]
        sum += len(set(one_list))
    return sum


def part2():
    sum = 0
    for group in inp_list:
        splitted = [set(ans) for ans in group.split("\n") if ans != ""]
        one_list = set.intersection(*splitted)
        sum += len(one_list)
    return sum


if __name__ == "__main__":
    print(part2())
