inp_f = open("input/day16.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n\n") if line != ""]


def part1():
    d = {}
    rules = [line for line in inp_list[0].split("\n") if line != ""]
    for rule in rules:
        this_rule = [[int(num) for num in nums.split("-")] for nums in rule.split(": ")[1].split(" or ")]
        for i in range(this_rule[0][0], this_rule[0][1]+1):
            d[i] = True
        for i in range(this_rule[1][0], this_rule[1][1]+1):
            d[i] = True
    
    acc = 0
    other_tickets = [[int(num) for num in line.split(",") if num != "nearby tickets:"] for line in inp_list[2].split("\n") if line != ""]
    for ticket in other_tickets:
        for num in ticket:
            if num not in d:
                acc += num
    return acc


def is_valid(d, ticket):
    for num in ticket:
        if num not in d:
            return False
    return True


def is_valid_field(rule, val):
    if val < rule[0][0] or val > rule[1][1]:
        return False
    if val > rule[0][1] and val < rule[1][0]:
        return False
    return True


def sort_valid_fields(fields):
    return len(fields[1])
    

def part2():
    d = {}
    rules = [[[int(num) for num in nums.split("-")] for nums in line.split(": ")[1].split(" or ")] for line in inp_list[0].split("\n") if line != ""]
    for rule in rules:
        for i in range(rule[0][0], rule[0][1]+1):
            d[i] = True
        for i in range(rule[1][0], rule[1][1]+1):
            d[i] = True

    my_ticket = [int(num) for num in inp_list[1].split("\n")[1].split(",")]
    
    other_tickets = [[int(num) for num in line.split(",") if num != "nearby tickets:"] for line in inp_list[2].split("\n") if line != ""]
    other_tickets[:] = [x for x in other_tickets[1:] if is_valid(d, x)]
    
    # determine valid fields for each position
    valid_fields = []
    for i in range(len(other_tickets[0])):
        valid_fields.append(list(range(len(rules))))
        for j in range(len(other_tickets)):
            valid_fields[i][:] = [field for field in valid_fields[i] if is_valid_field(rules[field], other_tickets[j][i])]

    enum_valid_fields = list(enumerate(valid_fields))
    enum_valid_fields.sort(key=sort_valid_fields)

    final_fields = {}  # maps field index to index of field in ticket
    for i, fields in enum_valid_fields:
        for field in fields:
            if field not in final_fields:
                final_fields[field] = i
                break
        else:
            print("error")

    final_ans = 1
    for i in range(6):
        final_ans *= my_ticket[final_fields[i]]
    return final_ans


if __name__ == "__main__":
    # print(part1())
    print(part2())
