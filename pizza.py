import numpy as np

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


# PROCESS THE PIZZA


# SAVE THE RESULT


def evaluate_slices(pizza):
    return None
