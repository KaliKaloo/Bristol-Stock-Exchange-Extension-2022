# from scipy.stats import cauchy
import numpy as np
import random

# F = random.sample(np.arange(-1,1), 8)
# print(F)


# Python3 program to demonstrate
# the use of sample() function .
  
# import random 
from random import sample
population = [1,2,3,4]
stratlist = [0,1,2,3]
x_i_stratval = 4

random.shuffle(stratlist)
x_r1_stratval = population[stratlist[0]]
while(x_r1_stratval == x_i_stratval):
    print("loop")
    print(x_r1_stratval)
    random.shuffle(stratlist)
    x_r1_stratval = population[stratlist[0]]

print(x_r1_stratval)