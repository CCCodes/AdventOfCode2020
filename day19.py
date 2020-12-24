import itertools


inp_f = open("input/day19.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n\n") if line != ""]


# returns all possibilities for that rule
def recurse(rules_dict, rule):
    rules_ = rules_dict[rule]
    if rules_[0] == '"':
        return [rules_[1]]
    rules = [nums.split(" ") for nums in rules_.split(" | ")]

    res = []
    for nums in rules:
        opts = []
        for num in nums:
            opts.append(recurse(rules_dict, num))
        for opt in itertools.product(*opts):
            res.append("".join(opt))
    return res


def part1():
    rules_dict = {}
    rules = [line.split(": ") for line in inp_list[0].split("\n") if line != "\n"]
    for rule in rules:
        rules_dict[rule[0]] = rule[1]
    possibilities = recurse(rules_dict, "0")

    instances = [line for line in inp_list[1].split("\n") if line != ""]
    count = 0
    for inst in instances:
        if inst in possibilities:
            count += 1
    return count


def part2():
    rules_dict = {}
    rules = [line.split(": ") for line in inp_list[0].split("\n") if line != "\n"]
    for rule in rules:
        rules_dict[rule[0]] = rule[1]

    # m+n instances of rule 42
    rule42 = recurse(rules_dict, '42')

    # followed by n instances of rule 31
    rule31 = recurse(rules_dict, '31')

    # where m, n >= 1

    possibilities = recurse(rules_dict, "0")
    instances = [line for line in inp_list[1].split("\n") if line != ""]
    count = 0
    for inst in instances:
        if inst in possibilities:
            count += 1
        else:
            next_idx = 0
            num42 = 0
            num31 = 0
            trying31 = False
            while True:
                if trying31:
                    for poss in rule31:
                        if inst[next_idx:next_idx+8] == poss:
                            num31 += 1
                            next_idx += 8
                            break
                    else:
                        if next_idx == len(inst) and num42 > num31 and num31 > 0:
                            count += 1
                        break

                else:
                    for poss in rule42:
                        if inst[next_idx:next_idx+8] == poss:
                            num42 += 1
                            next_idx += 8
                            break
                    else:
                        trying31 = True

    return count


if __name__ == "__main__":
    print(part1())
    print(part2())
