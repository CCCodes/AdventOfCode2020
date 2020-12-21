import copy



def part1():
    inp_f = open("input/day11.txt", "r")
    inp = inp_f.read()
    inp_list = [list(line) for line in inp.split("\n") if line != ""]
    while True:
        changed = False
        new_setup = copy.deepcopy(inp_list)
        for row in range(len(inp_list)):
            for col in range(len(inp_list[0])):
                if inp_list[row][col] == "L":
                    if row != 0 and inp_list[row-1][col] == "#":
                        continue
                    if row != len(inp_list)-1 and inp_list[row+1][col] == "#":
                        continue
                    if col != 0 and inp_list[row][col-1] == "#":
                        continue
                    if col != len(inp_list[0])-1 and inp_list[row][col+1] == "#":
                        continue
                    if row != 0 and col != 0 and inp_list[row-1][col-1] == "#":
                        continue
                    if row != 0 and col != len(inp_list[0])-1 and inp_list[row-1][col+1] == "#":
                        continue
                    if row != len(inp_list)-1 and col != 0 and inp_list[row+1][col-1] == "#":
                        continue
                    if row != len(inp_list)-1 and col != len(inp_list[0])-1 and inp_list[row+1][col+1] == "#":
                        continue
                    new_setup[row][col] = "#"
                    changed = True
                elif inp_list[row][col] == "#":
                    num_occupied = 0
                    if row != 0 and inp_list[row-1][col] == "#":
                        num_occupied += 1
                    if row != len(inp_list)-1 and inp_list[row+1][col] == "#":
                        num_occupied += 1
                    if col != 0 and inp_list[row][col-1] == "#":
                        num_occupied += 1
                    if col != len(inp_list[0])-1 and inp_list[row][col+1] == "#":
                        num_occupied += 1
                    if row != 0 and col != 0 and inp_list[row-1][col-1] == "#":
                        num_occupied += 1
                    if row != 0 and col != len(inp_list[0])-1 and inp_list[row-1][col+1] == "#":
                        num_occupied += 1
                    if row != len(inp_list)-1 and col != 0 and inp_list[row+1][col-1] == "#":
                        num_occupied += 1
                    if row != len(inp_list)-1 and col != len(inp_list[0])-1 and inp_list[row+1][col+1] == "#":
                        num_occupied += 1
                    if num_occupied >= 4:
                        new_setup[row][col] = "L"
                        changed = True
        if not changed:
            break
        inp_list = new_setup
    return sum([list1.count("#") for list1 in inp_list])


def count_spot(row, col, setup):
    num_occupied = 0

    # count upper left diag
    row_pos = row
    col_pos = col
    while row_pos > 0 and col_pos > 0:
        row_pos -= 1
        col_pos -= 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            num_occupied += 1
            break
    
    # count lower left diag
    row_pos = row
    col_pos = col
    while row_pos < len(setup)-1 and col_pos > 0:
        row_pos += 1
        col_pos -= 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            num_occupied += 1
            break
    
    # count upper right diag
    row_pos = row
    col_pos = col
    while row_pos > 0 and col_pos < len(setup[0])-1:
        row_pos -= 1
        col_pos += 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            num_occupied += 1
            break

    # count lower right diag
    row_pos = row
    col_pos = col
    while row_pos < len(setup)-1 and col_pos < len(setup[0])-1:
        row_pos += 1
        col_pos += 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            num_occupied += 1
            break
    
    # count up
    row_pos = row
    while row_pos > 0:
        row_pos -= 1
        if setup[row_pos][col] == "L":
            break
        if setup[row_pos][col] == "#":
            num_occupied += 1
            break

    # count down
    row_pos = row
    while row_pos < len(setup)-1:
        row_pos += 1
        if setup[row_pos][col] == "L":
            break
        if setup[row_pos][col] == "#":
            num_occupied += 1
            break
    
    # count left
    col_pos = col
    while col_pos > 0:
        col_pos -= 1
        if setup[row][col_pos] == "L":
            break
        if setup[row][col_pos] == "#":
            num_occupied += 1
            break
    
    # count right
    col_pos = col
    while col_pos < len(setup[0])-1:
        col_pos += 1
        if setup[row][col_pos] == "L":
            break
        if setup[row][col_pos] == "#":
            num_occupied += 1
            break
    
    return num_occupied


# return True if none occupied, False if found occupied
def count_spot_bool(row, col, setup):
    num_occupied = 0

    # count upper left diag
    row_pos = row
    col_pos = col
    while row_pos > 0 and col_pos > 0:
        row_pos -= 1
        col_pos -= 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            return False
    
    # count lower left diag
    row_pos = row
    col_pos = col
    while row_pos < len(setup)-1 and col_pos > 0:
        row_pos += 1
        col_pos -= 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            return False
    
    # count upper right diag
    row_pos = row
    col_pos = col
    while row_pos > 0 and col_pos < len(setup[0])-1:
        row_pos -= 1
        col_pos += 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            return False

    # count lower right diag
    row_pos = row
    col_pos = col
    while row_pos < len(setup)-1 and col_pos < len(setup[0])-1:
        row_pos += 1
        col_pos += 1
        if setup[row_pos][col_pos] == "L":
            break
        if setup[row_pos][col_pos] == "#":
            return False
    
    # count up
    row_pos = row
    while row_pos > 0:
        row_pos -= 1
        if setup[row_pos][col] == "L":
            break
        if setup[row_pos][col] == "#":
            return False

    # count down
    row_pos = row
    while row_pos < len(setup)-1:
        row_pos += 1
        if setup[row_pos][col] == "L":
            break
        if setup[row_pos][col] == "#":
            return False
    
    # count left
    col_pos = col
    while col_pos > 0:
        col_pos -= 1
        if setup[row][col_pos] == "L":
            break
        if setup[row][col_pos] == "#":
            return False
    
    # count right
    col_pos = col
    while col_pos < len(setup[0])-1:
        col_pos += 1
        if setup[row][col_pos] == "L":
            break
        if setup[row][col_pos] == "#":
            return False
    
    return True


def part2():
    inp_f = open("input/day11.txt", "r")
    inp = inp_f.read()
    inp_list = [list(line) for line in inp.split("\n") if line != ""]
    while True:
        changed = False
        new_setup = copy.deepcopy(inp_list)
        for row in range(len(inp_list)):
            for col in range(len(inp_list[0])):
                if inp_list[row][col] == "L":
                    if count_spot_bool(row, col, inp_list):
                        new_setup[row][col] = "#"
                        changed = True
                elif inp_list[row][col] == "#":
                    if count_spot(row, col, inp_list) >= 5:
                        new_setup[row][col] = "L"
                        changed = True
        if not changed:
            break
        inp_list = new_setup
    return sum([list1.count("#") for list1 in inp_list])


if __name__ == "__main__":
    # print(part1())
    print(part2())
