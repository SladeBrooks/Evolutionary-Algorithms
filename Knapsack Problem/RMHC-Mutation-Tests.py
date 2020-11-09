import numpy as np
import random
import copy
import pandas as pd
import matplotlib.pyplot as plt
from HillClimbers import HillClimbers

"""
    Optimization investigation of RMHC:
    Investigate the optimum mutation rate for my RMHCs using 2 different sets of climber population sizes
"""
#below is the optimization tests using 10 climbers
generations = 100
climbers = 10
hco1 = HillClimbers(climbers,items,max_vol)
mutation_tests = 5

mut_tests = [[] for x in range(mutation_tests)]
for k in range(mutation_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.mutate_all(k+1)
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(mutation_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Mutation Rate: {}'.format(i+1) for i in range(mutation_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Hill CLimber Optimization, Number of Climbers: 10')
plt.show()


#below is the optimization test using 100 climbers
#checking for high climber Rate
generations = 100
climbers = 100
hco1 = HillClimbers(climbers,items,max_vol)
mutation_tests = 5

mut_tests = [[] for x in range(mutation_tests)]
for k in range(mutation_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.mutate_all(k+1)
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(mutation_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Mutation Rate: {}'.format(i+1) for i in range(mutation_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Hill CLimber Optimization, Number of Climbers: 100')
plt.show()
