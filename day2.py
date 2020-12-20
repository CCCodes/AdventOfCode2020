inp_f = open("input/day2.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    count = 0
    for line in inp_list:
        parts = line.split(" ")
        rang = [int(num) for num in parts[0].split("-")]
        char = parts[1][0]
        pwd = parts[2]
        cnt = pwd.count(char)
        if rang[0] <= cnt and cnt <= rang[1]:
            count += 1
    return count


def part2():
    count = 0
    for line in inp_list:
        parts = line.split(" ")
        rang = [int(num) for num in parts[0].split("-")]
        char = parts[1][0]
        pwd = parts[2]
        if (pwd[rang[0]-1] == char) != (pwd[rang[1]-1] == char):
            count += 1
    return count


if __name__ == "__main__":
    print(part2())