inp = "1,0,16,5,17,4"
inp_list = [int(num) for num in inp.split(",")]


def part1():
    for _ in range(7, 2021):
        try:
            found = inp_list[:-1][::-1].index(inp_list[-1])
        except ValueError:
            inp_list.append(0)  # new num
            continue
        this_idx = len(inp_list) - 1
        prev_idx = len(inp_list) - 2 - found
        inp_list.append(this_idx - prev_idx)
    return inp_list[-1]


def part2():
    d = {}
    for i, num in enumerate(inp_list[:-1]):
        d[num] = i+1    
    last_one = inp_list[-1]
    for i in range(7, 30000001):
        if last_one not in d:
            d[last_one] = i - 1
            last_one = 0
            continue
        new_last_one = i-1-d[last_one]
        d[last_one] = i - 1
        last_one = new_last_one
    return last_one


if __name__ == "__main__":
    print(part1())
    print(part2())
