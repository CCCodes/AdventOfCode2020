inp_f = open("input/day5.txt", "r")
inp = inp_f.read()
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    highest_seat = -1
    for line in inp_list:
        rang = [0, 128]
        for c in line[:7]:
            change = (rang[1] - rang[0]) / 2
            if c == "F":
                rang[1] -= change
            if c == "B":
                rang[0] += change
        row = rang[0]
        rang_col = [0, 8]
        for c in line[7:]:
            change = (rang_col[1] - rang_col[0]) / 2
            if c == "L":
                rang_col[1] -= change
            if c == "R":
                rang_col[0] += change
        col = rang_col[0]
        seat_id = row * 8 + col
        if seat_id > highest_seat:
            highest_seat = seat_id
    return highest_seat


def part2():
    all_seats = []
    for line in inp_list:
        rang = [0, 128]
        for c in line[:7]:
            change = (rang[1] - rang[0]) / 2
            if c == "F":
                rang[1] -= change
            if c == "B":
                rang[0] += change
        row = rang[0]
        rang_col = [0, 8]
        for c in line[7:]:
            change = (rang_col[1] - rang_col[0]) / 2
            if c == "L":
                rang_col[1] -= change
            if c == "R":
                rang_col[0] += change
        col = rang_col[0]
        seat_id = row * 8 + col
        all_seats.append(seat_id)
    all_seats.sort()
    for i in range(len(all_seats)-1):
        if all_seats[i] + 2 == all_seats[i+1]:
            return all_seats[i] + 1


if __name__ == "__main__":
    print(part2())
