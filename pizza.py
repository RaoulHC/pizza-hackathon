import numpy as np
from itertools import permutations
from Minimize import  find_lstar ,factors ,find_slice ,find_minimum_sized_slices

# LOAD THE INPUT 
with open('example.in','r') as f:
    lines = f.readlines()

# First line is R C L H 
nums = [int(s) for s in lines[0].split(' ')]
R,C,L,H = nums[0],nums[1],nums[2],nums[3]
print "R = ", R
print "C = ", C
print "L = ", L
print "H = ", H

# Now get the pizza as a matrix
pizza = []
for line in lines[1:]:
    line = line.replace('T','0 ')
    line = line.replace('M','1 ')
    line = line.replace('\n','')
    line = line[:-1]

    pizza.append([ int(s) for s in line.split(' ')])

# convert to a numpy array 
pizza = np.array(pizza)
print "PIZZA: "
print pizza

#find  K
N_1 = np.count_nonzero(pizza)
N_0 = pizza.shape[0]*pizza.shape[1] - N_1
K = min(N_0,N_1)
type_of_k = 0 if N_0 < N_1 else 1

print "K = ",K 

#form pairs from the factor list
f_list =  factors(2*L)
pair_list = []
for i in xrange(int(len(f_list)/2)):
    pair_list.append( [f_list[i],f_list[-(i+1)] ] )
    pair_list.append( [f_list[-(i+1)],f_list[i] ] )

# Evaluate the seed locations for the possilbe arrays
l_star_locations = find_lstar(pizza, type_of_k)

for slice_size in pair_list:
    print "Evaluation minimum sized solution: ", slice_size

    # slices[pref], marked_pizza = 
    slices = find_minimum_sized_slices(pizza,slice_size, l_star_locations,L,H)
    print "FOUND ", len(slices), " SLICES:"
    print slices
    #
    # solution[pref] = maximise(pizza,marked_pizza, slices[pref])


# SAVE THE RESULT
