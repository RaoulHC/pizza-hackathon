# maximise function

import itertools
import numpy as np
import random

# return slice_list?
H = 10

# slice list
def maximise(marked_pizza, slice_list):
#    for slice in slice_list:
#	try_extend(slice)
    pass

def find_non_slice(marked_pizza):
    """ Return list of indices of non slice bits
    """
    non_slice_list = []
    for index in np.ndindex(marked_pizza.shape):
	# maker_pizza(index) != 2
        if marked_pizza[index] != 2:
            non_slice_list.append(index)

    return non_slice_list

def try_extend((x1, y1, x2, y2), marked_pizza):
    """ update slice and pizza """
    # look around the slice (x1 y1 x2 y2)
    # NOTE we might need to check for swapsies
    # new_slice = (x1-1, y1, x2, y2)

    # check possible ways to extend
    size = (x2 - x1 + 1) * (y2 - y1 + 1)
    if ((y2 - y1 + 1) + size) < H:
        a = check_area((x1-1, y1, x1-1, y2), marked_pizza)
        c = check_area((x2+1, y1, x2+1, y2), marked_pizza)
    else:
        a = None
        c = None

    if ((x2 - x1 + 1) + size) < H:
        b = check_area((x1, y1-1, x2, y1-1), marked_pizza)
        d = check_area((x1, y2+1, x2, y2+1), marked_pizza)
    else:
        b = None
        d = None

    print a, b, c, d

    # got whether left up right down are possible to extend into
    # want to kind of recursive go down extensions
    # NOTE can be optimised
    valid_extensions = []
    for i in (a, b, c, d):
        if i is not None:
            valid_extensions.append(i)

    if valid_extensions == []:
        return ((x1, y1, x2, y2), marked_pizza)

    rand_choice = random.randint(0, len(valid_extensions))
    chosen_extension = valid_extensions[rand_choice]

    print chosen_extension


def check_area((x1, y1, x2, y2), marked_pizza):
    """ look over each indice in rectangle and check it's not 2 """
    # slice (x1 y1 x2 y2)
    if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
        print "no negative values"
        return None
    try:
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # print i, j
                # print marked_pizza[(i, j)]
                if marked_pizza[(i, j)] == 2:
                   return None
        return (x1, y1, x2, y2)
    except Exception as e:
        print e
        return None


def find_extendables(slice_list, marked_pizza):
    """ find a list of slices which can be extended """
    # for slice in slice_list:
    # try extensions by increases indice
    pass

if __name__ == '__main__':
    a = np.array(
            [(1,1),
                (2,2)])
    print a
    # print find_non_slice(a)

    # check = (0, 0, 0, 1)
    # print check_area(check, a)

    pizza_slice = (1, 0, 1, 1)
    try_extend(pizza_slice, a)
