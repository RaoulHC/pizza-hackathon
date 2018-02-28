import numpy as np
from itertools import permutations
from Minimize import  minimize

# LOAD THE INPUT 
with open('harder_example.in','r') as f:
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
print "K = ",K 

# PROCESS THE PIZZA
prefence_list = []
perms = set()
for perm in permutations([1,2,3,4]):
    perms.add(perm)

for pref in perms:
    print "Evaluation permuation: ", pref

    # 
    slices[pref], marked_pizza = minimize(pizza,pref)

    #
    solution[pref] = maximise(pizza,marked_pizza, slices[pref])


# SAVE THE RESULT
