from copy import deepcopy 

def find_lstar(pizza,l_type):
    """
    """
    distance = max(pizza.shape[0],pizza.shape[1] )
    lstar_locations = []

    #
    for x in xrange(pizza.shape[0]):
        for y in xrange(pizza.shape[1]):
            if l_type == pizza[x,y]:
                # find the distance from the edge 
                distance = 0
                distance += max(x,pizza.shape[0]/2-x)
                distance += max(y,pizza.shape[1]/2-y)
                lstar_locations.append( [ x,y, distance ])
    return lstar_locations

def factors(n):
    f_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            f_list.append(i)

    return f_list 

def find_slice(pizza,l_star,direction,L,H):
    # Find tha
    pass 


def get_possible_slices(pizza, star_loc, slice_size, L):
    # 
    possible_slices = []
    X,Y = star_loc[0], star_loc[1]

    for x_offset in xrange(slice_size[0]):
        X = star_loc[0] - (x_offset)
        if X < 0:
            break

        for y_offset in xrange(slice_size[1]):
            Y = star_loc[1] - y_offset

            if Y < 0:
                break

            n_0,n_1 = 0,0
            for x in xrange(slice_size[0]): 
                if x + X > pizza.shape[1]:
                    break

                for y in xrange(slice_size[1]):
                    if y + Y > pizza.shape[0]:
                        break


                    # does it already have a thing 
                    if pizza[x+X,y+Y] == 2:
                        break
                    elif pizza[x+X,y+Y] == 0:
                        n_0 += 1
                    elif pizza[x+X,y+Y] == 1:
                        n_1 += 1

            # At this poitn we have a thing whihc does 
            if n_1 < L or n_0 < L:
                break
            else:
                possible_slices.append( [(X,Y),(X+slice_size[0]-1,Y+slice_size[1]-1)])
    return possible_slices

def slice_could_be_placed(pizza,slice_size):
    """
    """
    for x in xrange(pizza.shape[0]):
        for y in xrange(pizza.shape[1]):

            if l_type == pizza[x,y]:
                pass

def remove_slice_from_pizza(pizza,p_slice):
    # print "removing",p_slice[0][0],":",p_slice[1][0] 
    # print "removing",p_slice[0][1],":",p_slice[1][1] 

        # pizza[p_slice[0][0]:p_slice[1][0],p_slice[0][1]:p_slice[1][1]] = 2

    for x in xrange(p_slice[0][0], p_slice[1][0]+1):
        for y in xrange(p_slice[0][1], p_slice[1][1]+1):
            pizza[x,y] = 2
    return pizza

def find_minimum_sized_slices(pizza, slice_size, l_star_locations, L, H):

    # First get a list of initial slicing 
    if len(l_star_locations) == 0:
        return []

    total_slices = []
    start_loc = l_star_locations[0]
    pizza_slices = get_possible_slices(pizza, start_loc, slice_size, L)

    # Next go through each pizza slice and find the list of slies that it could be paired with
    for pizza_slice in pizza_slices:
        slim_pizza = remove_slice_from_pizza(deepcopy(pizza), pizza_slice)

        # And another list of possible slices
        next_iterations_slices = find_minimum_sized_slices(slim_pizza,  
                                                           slice_size,
                                                           l_star_locations[1:],
                                                           L,
                                                           H)

        if next_iterations_slices == []:
            print "SOLUTION"
            print slim_pizza
            print ""
            total_slices.append(pizza_slice)
            continue

        for next_slice in next_iterations_slices:
            total_slices.append([pizza_slice] +  next_slice)
    
    return total_slices