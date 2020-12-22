import math

inp_f = open("input/day13.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    earliest_time = int(inp_list[0])
    ids = [int(num) for num in inp_list[1].split(",") if num != "x"]
    best_id = None
    best_time = None
    for num in ids:
        dividend = math.ceil(earliest_time / num)
        this_time = num * dividend
        if best_time is None or best_time > this_time:
            best_time = this_time
            best_id = num
    return (best_time - earliest_time) * best_id


def part2():
    ids = [int(num) for num in inp_list[1].split(",") if num != "x"]
    idxs = [i for i, num in enumerate(inp_list[1].split(",")) if num != "x"]
    inc_idx = 0
    inc = ids[inc_idx]

    comp = 0
    while True:
        if (comp + idxs[inc_idx+1]) % ids[inc_idx+1] == 0:
            inc_idx += 1
            inc *= ids[inc_idx]
            if inc_idx == len(ids)-1:
                return comp
        comp += inc


if __name__ == "__main__":
    # print(part1())
    print(part2())
