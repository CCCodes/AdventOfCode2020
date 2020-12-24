import itertools

import numpy as np


inp_f = open("input/day17.txt", "r")
inp = inp_f.read()
# inp = ".#.\n..#\n###\n"
inp_list = [line for line in inp.split("\n") if line != ""]


def part1():
    arr = np.zeros((1, len(inp_list), len(inp_list[0])))
    for i, line in enumerate(inp_list):
        for j, sym in enumerate(line):
            if sym == "#":
                arr[0,i,j] = 1
    for _ in range(6):
        # copy to check
        new_arr = np.zeros((np.array(arr.shape)+2))
        new_arr[1:-1,1:-1,1:-1] = arr
        
        # copy to modify
        arr = new_arr.copy()

        for x in range(new_arr.shape[1]):
            for y in range(new_arr.shape[2]):
                for z in range(new_arr.shape[0]):
                    surround = itertools.product([z-1, z, z+1], [x-1, x, x+1], [y-1, y, y+1])
                    num_blocks = 0
                    for coord in surround:
                        if coord[0] == -1 or coord[1] == -1 or coord[2] == -1:
                            continue
                        try:
                            if new_arr[coord] == 1:
                                num_blocks += 1
                        except IndexError:
                            pass
                    if new_arr[z,x,y] == 1:
                        num_blocks -= 1  # don't count self
                        if num_blocks != 2 and num_blocks != 3:
                            arr[z,x,y] = 0
                    elif new_arr[z,x,y] == 0:
                        if num_blocks == 3:
                            arr[z,x,y] = 1
        # don't let array keep growing where 0
        if np.count_nonzero(arr[0,:,:]) == 0:
            arr = arr[1:,:,:]
        if np.count_nonzero(arr[-1,:,:]) == 0:
            arr = arr[:-1,:,:]
        if np.count_nonzero(arr[:,0,:]) == 0:
            arr = arr[:,1:,:]
        if np.count_nonzero(arr[:,-1,:]) == 0:
            arr = arr[:,:-1,:]
        if np.count_nonzero(arr[:,:,0]) == 0:
            arr = arr[:,:,1:]
        if np.count_nonzero(arr[:,:,-1]) == 0:
            arr = arr[:,:,:-1]
    return arr.sum()


def part2():
    arr = np.zeros((1, 1, len(inp_list), len(inp_list[0])))
    for i, line in enumerate(inp_list):
        for j, sym in enumerate(line):
            if sym == "#":
                arr[0,0,i,j] = 1
    for _ in range(6):
        # copy to check
        new_arr = np.zeros((np.array(arr.shape)+2))
        new_arr[1:-1,1:-1,1:-1,1:-1] = arr
        
        # copy to modify
        arr = new_arr.copy()

        for x, y, z, w in itertools.product(range(new_arr.shape[2]), range(new_arr.shape[3]), range(new_arr.shape[0]), range(new_arr.shape[1])):
            surround = itertools.product([z-1, z, z+1], [w-1, w, w+1], [x-1, x, x+1], [y-1, y, y+1])
            num_blocks = 0
            for coord in surround:
                if coord[0] == -1 or coord[1] == -1 or coord[2] == -1 or coord[3] == -1:
                    continue
                try:
                    if new_arr[coord] == 1:
                        num_blocks += 1
                except IndexError:
                    pass
            if new_arr[z,w,x,y] == 1:
                num_blocks -= 1  # don't count self
                if num_blocks != 2 and num_blocks != 3:
                    arr[z,w,x,y] = 0
            elif new_arr[z,w,x,y] == 0:
                if num_blocks == 3:
                    arr[z,w,x,y] = 1
        # don't let array keep growing where 0
        if np.count_nonzero(arr[0,:,:,:]) == 0:
            arr = arr[1:,:,:,:]
        if np.count_nonzero(arr[-1,:,:,:]) == 0:
            arr = arr[:-1,:,:,:]
        if np.count_nonzero(arr[:,0,:,:]) == 0:
            arr = arr[:,1:,:,:]
        if np.count_nonzero(arr[:,-1,:,:]) == 0:
            arr = arr[:,:-1,:,:]
        if np.count_nonzero(arr[:,:,0,:]) == 0:
            arr = arr[:,:,1:,:]
        if np.count_nonzero(arr[:,:,-1,:]) == 0:
            arr = arr[:,:,:-1,:]
        if np.count_nonzero(arr[:,:,:,0]) == 0:
            arr = arr[:,:,:,1:]
        if np.count_nonzero(arr[:,:,:,-1]) == 0:
            arr = arr[:,:,:,:-1]
    return arr.sum()


if __name__ == "__main__":
    print(part2())
