inp_f = open("input/day18.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def find_close(s):
    count = 0
    for i, c in enumerate(s):
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
            if count == 0:
                return i


def evaluate(s, prev_num=None, op=None):
    if s[0] == "(":
        close = find_close(s)
        op_idx = close + 2
        first_num = evaluate(s[1:close])
    else:
        first_num = s[0]
        op_idx = 2
    if op == "+":
        after_op = prev_num + int(first_num)
    elif op == "*":
        after_op = prev_num * int(first_num)
    else:
        after_op = int(first_num)
    try:
        new_op = s[op_idx]
    except IndexError:
        return str(after_op)
    return evaluate(s[op_idx+2:], after_op, new_op)


def part1():
    nums = []
    for line in inp_list:
        nums.append(int(evaluate(line)))
    return sum(nums)


def evaluate2(s, prev_num=None, op=None):
    if s[0] == "(":
        close = find_close(s)
        op_idx = close + 2
        first_num = evaluate2(s[1:close])
    else:
        first_num = s[0]
        op_idx = 2
    next_idx = op_idx + 2
    
    last_one = False
    add_first = False
    try:
        new_op = s[op_idx]
        if op == "*" and new_op == "+":
            first_num = evaluate2(s[next_idx:], int(first_num), new_op)
            add_first = True
    except IndexError:
        last_one = True

    if op == "+":
        after_op = prev_num + int(first_num)
    elif op == "*":
        after_op = prev_num * int(first_num)
    else:
        after_op = int(first_num)
    if last_one or add_first:
        return str(after_op)
    
    return evaluate2(s[op_idx+2:], after_op, new_op)


def part2():
    nums = []
    for line in inp_list:
        nums.append(int(evaluate2(line)))
    return sum(nums)


if __name__ == "__main__":
    print(part1())
    print(part2())
