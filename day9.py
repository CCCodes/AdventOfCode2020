inp_f = open("input/day9.txt", "r")
inp = inp_f.read()
inp_list = [int(line) for line in inp.split("\n") if line != ""]


def part1():
    for i in range(25, len(inp_list)):
        preamble = inp_list[i-25:i]
        found = False
        for num in preamble:
            if inp_list[i] - num in preamble:
                if num * 2 == inp_list[i] and preamble.count(num) < 2:
                    continue
                found = True
        if not found:
            return inp_list[i]


def part2(sum_to):
    for i in range(len(inp_list)):
        for j in range(i+2, len(inp_list)):
            if sum(inp_list[i:j]) == sum_to:
                return max(inp_list[i:j]) + min(inp_list[i:j])


if __name__ == "__main__":
    print(part1())  # 26796446
    print(part2(26796446))
