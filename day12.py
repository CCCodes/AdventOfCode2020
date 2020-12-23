inp_f = open("input/day12.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    ns_pos = 0
    ew_pos = 0
    facing = "E"
    for instr in inp_list:
        action = instr[0]
        value = int(instr[1:])
        if action == "N":
            ns_pos += value
        if action == "S":
            ns_pos -= value
        if action == "E":
            ew_pos += value
        if action == "W":
            ew_pos -= value
        if action == "L":
            while value > 0:
                if facing == "N":
                    facing = "W"
                elif facing == "W":
                    facing = "S"
                elif facing == "S":
                    facing = "E"
                elif facing == "E":
                    facing = "N"
                value -= 90
        if action == "R":
            while value > 0:
                if facing == "N":
                    facing = "E"
                elif facing == "E":
                    facing = "S"
                elif facing == "S":
                    facing = "W"
                elif facing == "W":
                    facing = "N"
                value -= 90
        if action == "F":
            if facing == "N":
                ns_pos += value
            if facing == "E":
                ew_pos += value
            if facing == "S":
                ns_pos -= value
            if facing == "W":
                ew_pos -= value

    return abs(ns_pos) + abs(ew_pos)


def part2():
    ship = [0, 0]
    wp = [1, 10]
    for instr in inp_list:
        action = instr[0]
        value = int(instr[1:])
        if action == "N":
            wp[0] += value
        if action == "S":
            wp[0] -= value
        if action == "E":
            wp[1] += value
        if action == "W":
            wp[1] -= value
        if action == "L":
            while value > 0:
                old_wp = wp.copy()
                wp[1] = -old_wp[0]
                wp[0] = old_wp[1]
                value -= 90
        if action == "R":
            while value > 0:
                old_wp = wp.copy()
                wp[1] = old_wp[0]
                wp[0] = -old_wp[1]
                value -= 90
        if action == "F":
            ship[0] += wp[0] * value
            ship[1] += wp[1] * value

    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    # print(part1())
    print(part2())
