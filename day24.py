import numpy as np


def get_coords(line):
    tile = [0, 0]
    idx = 0
    while idx < len(line):
        if line[idx] == "e" or line[idx] == "w":
            direction = line[idx]
            idx += 1
        elif line[idx] == "n" or line[idx] == "s":
            direction = line[idx:idx+2]
            idx += 2
        if direction == "e":
            tile[1] -= 2
        elif direction == "w":
            tile[1] += 2
        else:
            if direction[1] == "e":
                tile[1] -= 1
            elif direction[1] == "w":
                tile[1] += 1
            if direction[0] == "s":
                tile[0] += 1
            if direction[0] == "n":
                tile[0] -= 1
    return str(tile[0]) + "," + str(tile[1])


def get_tiles():
    inp_f = open("input/day24.txt", "r")
    inp = inp_f.read()
    inp_list = [line for line in inp.split("\n") if line != ""]
    tiles = {}
    for line in inp_list:
        hash_coord = get_coords(line)
        if hash_coord in tiles and tiles[hash_coord]:
            tiles[hash_coord] = False
        else:
            tiles[hash_coord] = True
    return tiles


def flip_tiles(tile_arr):
    new_tile_arr = tile_arr.copy()
    neighbors = [(0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(len(tile_arr)):
        for j in range(len(tile_arr[i])):
            count_black = 0
            for neighbor in neighbors:
                try:
                    if tile_arr[i+neighbor[0], j+neighbor[1]] == 1:
                        count_black += 1
                except IndexError:  # white neighbor
                    pass
            if tile_arr[i, j] == 1:  # black tile
                if count_black == 0 or count_black > 2:
                    new_tile_arr[i, j] = 0
            if tile_arr[i, j] == 0:  # white tile
                if count_black == 2:
                    new_tile_arr[i, j] = 1
    return new_tile_arr


def part1():
    tiles = get_tiles()
    return sum(tiles.values())


def part2():
    tiles = get_tiles()
    max_x = None
    min_x = None
    max_y = None
    min_y = None
    for hash_coord in tiles:
        x, y = [int(num) for num in hash_coord.split(",")]
        if max_x is None or x > max_x:
            max_x = x
        if min_x is None or x < min_x:
            min_x = x
        if max_y is None or y > max_y:
            max_y = y
        if min_y is None or y < min_y:
            min_y = y

    # array of tiles, value 0 means white
    arr = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
    for hash_coord in tiles:
        if tiles[hash_coord]:
            x, y = [int(num) for num in hash_coord.split(",")]
            if min_x < 0:
                x -= min_x
            if min_y < 0:
                y -= min_y
            arr[x, y] = 1
    tiles_arr = np.zeros((max_x - min_x + 201, max_y - min_y + 201))
    tiles_arr[100:-100, 100:-100] = arr
    
    for _ in range(100):
        tiles_arr = flip_tiles(tiles_arr)
    return np.sum(tiles_arr)
            

if __name__ == "__main__":
    print(part1())
    print(part2())
