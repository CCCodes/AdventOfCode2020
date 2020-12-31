public_keys = [14222596, 4057428]


def part1():
    loop_size_ctr = [0, 0]

    for i, pk in enumerate(public_keys):
        value = 1
        subject_num = 7
        while True:
            if value == pk:
                break
            value *= subject_num
            value = value % 20201227
            loop_size_ctr[i] += 1

    subject_num = public_keys[0]
    loop_size = loop_size_ctr[1]
    value = 1
    for _ in range(loop_size):
        value *= subject_num
        value = value % 20201227
    return value


if __name__ == "__main__":
    print(part1())
