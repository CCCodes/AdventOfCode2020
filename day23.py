def cfg_as_str(config):
    start = 1
    next_cup = start
    res = []
    while True:
        next_cup = config[next_cup][1]
        if next_cup == start:
            return "".join([str(num) for num in res])
        res.append(next_cup)


def simulate(config, num_moves, current):
    num_cups = len(config)
    for _ in range(num_moves):
        prev, next1 = config[current]
        next2 = config[next1][1]
        next3 = config[next2][1]
        config[current] = [prev, config[next3][1]]
        picked_up = [next1, next2, next3]

        dest = current - 1
        while True:
            if dest <= 0:
                dest = num_cups
            if dest not in picked_up:
                dest_prev, dest_next = config[dest]
                config[dest] = [dest_prev, next1]
                config[next1] = [dest, next2]
                config[next2] = [next1, next3]
                config[next3] = [next2, dest_next]
                break
            dest -= 1
        current = config[current][1]
    return config


def part1():
    NUM_MOVES = 100
    config_list = [int(num) for num in list("962713854")]
    config = {}
    for i in range(len(config_list)):
        if i == len(config_list) - 1:
            config[config_list[i]] = [config_list[i-1], config_list[0]]
        elif i == 0:
            config[config_list[i]] = [config_list[-1], config_list[i+1]]
        else:
            config[config_list[i]] = [config_list[i-1], config_list[i+1]]
    simulate(config, NUM_MOVES, config_list[0])
    return cfg_as_str(config)


def part2():
    NUM_CUPS = 1000000
    NUM_MOVES = 10000000
    config_list = [int(num) for num in list("962713854")]
    config = {}  # store what number is prev and next in the ordering
    for i in range(1, len(config_list)):
        if i == len(config_list) - 1:
            config[config_list[i]] = [config_list[i-1], len(config_list) + 1]
        else:
            config[config_list[i]] = [config_list[i-1], config_list[i+1]]
    config[len(config_list)+1] = [config_list[-1], len(config_list)+2]
    for i in range(len(config_list)+2, NUM_CUPS):
        config[i] = [i-1, i+1]
    config[NUM_CUPS] = [NUM_CUPS-1, config_list[0]]
    config[config_list[0]] = [NUM_CUPS, config_list[1]]
    simulate(config, NUM_MOVES, config_list[0])

    next1 = config[1][1]
    next2 = config[next1][1]
    return next1 * next2


if __name__ == "__main__":
    print(part1())
    print(part2())
