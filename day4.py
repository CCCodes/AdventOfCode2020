import re


def part1(inp_list):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for passport in inp_list:
        fields1 = [line.split(" ") for line in passport.split("\n")]
        fields = [j.split(":")[0] for i in fields1 for j in i]
        for field in req_fields:
            if field not in fields:
                break
        else:
            valid += 1
    return valid


def part2(inp_list):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ecl_opts = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = 0
    for passport in inp_list:
        fields1 = [line.split(" ") for line in passport.split("\n")]
        fields1 = [j for i in fields1 for j in i]
        fields1 = [i.split(":") for i in fields1]
        fields = {}
        for f in fields1:
            # splitting on : doesn't yield two things
            # will continue to next field, but going through req_fields will miss that field
            if len(f) != 2:
                continue
            fields[f[0]] = f[1]
        if len(fields) < 7:
            continue
        for field in req_fields:
            if field not in fields:
                break
            if field == 'byr':
                if len(fields[field]) != 4:
                    break
                if re.match('^[0-9]*$', fields[field]) is None:
                    break
                if int(fields[field]) < 1920 or int(fields[field]) > 2002:
                    break
            if field == 'iyr':
                try:
                    if int(fields[field]) < 2010 or int(fields[field]) > 2020:
                        break
                except ValueError:
                    break
            if field == 'eyr':
                try:
                    if int(fields[field]) < 2020 or int(fields[field]) > 2030:
                        break
                except ValueError:
                    break
            if field == 'hgt':
                if len(fields[field]) < 4:
                    break
                unit = fields[field][-2:]
                if fields[field][-2:] != 'cm' and fields[field][-2:] != 'in':
                    break
                num_str = fields[field][:-2]
                try:
                    num = int(num_str)
                    if unit == 'cm' and (num < 150 or num > 193):
                        break
                    if unit == 'in' and (num < 59 or num > 76):
                        break
                except ValueError:
                    break
            if field == 'hcl':
                if len(fields[field]) != 7:
                    break
                if fields[field][0] != '#':
                    break
                if re.match("^[a-f0-9]*$", fields[field][1:]) is None:
                    break
            if field == 'ecl':
                if fields[field] not in ecl_opts:
                    break
            if field == 'pid':
                if len(fields[field]) != 9:
                    break
                try:
                    _ = int(fields[field])
                except ValueError:
                    break

        else:
            valid += 1
    return valid


if __name__ == "__main__":
    inp_f = open("day4.txt", "r")
    inp = inp_f.read()
    inp_list = [line for line in inp.split("\n\n") if line != ""]
    print(part2(inp_list))
