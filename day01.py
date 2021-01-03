inp_f = open("input/day1.txt", "r")
inp = inp_f.read()
inp_list = [int(num_str) for num_str in inp.split("\n") if num_str != ""]


def part1():
    for num in inp_list:
        if num == 1010:
            print("1010, double check")
        if 2020 - num in inp_list:
            return num * (2020 - num)


def part2():
    for i, num1 in enumerate(inp_list):
        for j, num2 in enumerate(inp_list):
            if j == i:
                continue
            num3 = 2020 - num1 - num2
            if num3 in inp_list:
                if num3 == num1 and num3 == num2:
                    if inp_list.count(num3) < 3:
                        continue
                elif num3 == num1 or num3 == num2:
                    if inp_list.count(num3) == 1:
                        continue
                return num3 * num1 * num2


if __name__ == "__main__":
    print(part2())
