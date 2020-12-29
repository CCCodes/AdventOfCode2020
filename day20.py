import functools

import numpy as np


TILE_SIZE = 8
PUZZLE_SIZE = 12
ACTIONS = [
    lambda tile: tile,
    lambda tile: np.rot90(tile),
    lambda tile: np.rot90(tile),
    lambda tile: np.rot90(tile),
    lambda tile: np.flip(tile, axis=0),
    lambda tile: np.rot90(tile),
    lambda tile: np.rot90(tile),
    lambda tile: np.rot90(tile)
]


def get_orientations(tile):
    orientations = []
    for action in ACTIONS:
        tile = action(tile)
        orientations.append(tile)
    return orientations


def check_valid(puzzle_list, tile):
    idx = len(puzzle_list)
    if idx % PUZZLE_SIZE != 0:
        left_tile = puzzle_list[-1]
        edge1 = left_tile[:, -1]
        edge2 = tile[:, 0]
        if not np.array_equal(edge1, edge2):
            return False

    if idx - PUZZLE_SIZE  >= 0:
        above_tile = puzzle_list[len(puzzle_list)-PUZZLE_SIZE]
        edge1 = above_tile[-1]
        edge2 = tile[0]
        if not np.array_equal(edge1, edge2):
            return False

    return True


def order_tiles(tiles, puzzle_list, visited):
    if len(puzzle_list) == len(tiles):
        return puzzle_list, visited

    for tile_id, orientations in tiles.items():
        if tile_id not in visited:
            for tile in orientations:
                if check_valid(puzzle_list, tile):
                    try_next = order_tiles(tiles, puzzle_list + [tile], visited + [tile_id])
                    if try_next is not None:
                        return try_next
    return None


def arrange_puzzle():
    inp_f = open("input/day20.txt", "r")
    inp = inp_f.read()
    inp_list = [line for line in inp.split("\n\n") if line != ""]
    tile_id_to_arr = {}
    for tile in inp_list:
        lines = [line for line in tile.split("\n") if line != ""]
        original = np.array([list(line) for line in lines[1:]])
        tile_id_to_arr[lines[0].split(" ")[1][:-1]] = original
    tile_id_to_orientations = {}
    for tile_id, tile in tile_id_to_arr.items():
        tile_id_to_orientations[tile_id] = get_orientations(tile)
    puzzle_list, visited = order_tiles(tile_id_to_orientations, [], [])
    idx = 0
    puzzle = np.empty((PUZZLE_SIZE * TILE_SIZE, PUZZLE_SIZE * TILE_SIZE), dtype=str)
    puzzle_id = []
    for row in range(0, PUZZLE_SIZE * TILE_SIZE, TILE_SIZE):
        puzzle_id.append([])
        for col in range(0, PUZZLE_SIZE * TILE_SIZE, TILE_SIZE):
            puzzle_id[-1].append(visited[idx])
            puzzle[row:row+TILE_SIZE,col:col+TILE_SIZE] = puzzle_list[idx][1:-1,1:-1]
            idx += 1
    return puzzle, puzzle_id


def is_monster(arr, monster):
    all_pound = np.full(monster.shape, "#", dtype=str)
    monster_true = all_pound == monster
    return ((arr == monster) == monster_true).all()


def count_monsters(orig_puzzle, monster):
    puzzles = get_orientations(orig_puzzle)
    counts = []
    for puzzle in puzzles:
        count = 0
        for i in range(puzzle.shape[0] - monster.shape[0]):
            for j in range(puzzle.shape[1] - monster.shape[1]):
                test_monster = puzzle[i:i+monster.shape[0], j:j+monster.shape[1]]
                if is_monster(test_monster, monster):
                    count += 1
        counts.append(count)
    return max(counts)


def part1(puzzle_id):
    corners = [puzzle_id[0][0], puzzle_id[0][-1], puzzle_id[-1][0], puzzle_id[-1][-1]]
    return functools.reduce(lambda a,b : int(a)*int(b), corners)
    

def part2(puzzle):
    monster = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "
    monster_arr = np.array([list(row) for row in monster.split("\n")])
    num_monsters = count_monsters(puzzle, monster_arr)
    return np.count_nonzero(puzzle == "#") - num_monsters * np.count_nonzero(monster_arr == "#")


if __name__ == "__main__":
    puzzle, puzzle_id = arrange_puzzle()
    print(part1(puzzle_id))
    print(part2(puzzle))
