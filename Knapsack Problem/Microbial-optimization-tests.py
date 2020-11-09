import numpy as np
import random
import copy
import pandas as pd
import matplotlib.pyplot as plt
from HillClimbers import HillClimbers

B = [3,54,55,32,50,26,70,7,45,1,40,28,46,16,20,15,56,98,13,66,29,64,96,91,97,99,94,51,27,30,43,9,14,62,92,76,37,85,23,52,67,39,82,42,8,25,44,31,11,100,74,75,60,93,73,36,35,77,78,24,84,61,19,88,49,18,90,22,89,68,81,59,57,65,58,63,4,72,69,41,80,10,83,5,79,53,95,21,6,17,87,38,33,12,71,86,47,34,48,2]
#volume
V = [6,8,5,10,8,6,7,14,11,9,14,6,12,12,10,6,10,7,6,7,13,5,7,5,9,5,13,6,5,8,9,6,14,8,7,5,7,5,10,12,11,5,5,12,14,10,6,13,8,7,12,5,5,11,11,10,12,12,12,7,11,10,8,5,12,8,11,12,6,6,10,9,13,12,12,5,5,5,12,14,11,6,12,6,6,11,8,11,12,10,12,7,12,14,13,5,8,8,11,10];
items = [(B[i],V[i]) for i in range(len(B))]
max_vol = 50

"""
    Optimization investigation of Microbial:
    Investigate the optimum pCrossover and pMutate rate for my microbial GA

"""
#Checking for optimal mutation Rate low climbers
generations = 1000
climbers = 10
hco1 = HillClimbers(climbers,items,max_vol)
mut_tests = 5

mut_tests = [[] for x in range(mut_tests)]
for k in range(mut_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.tournament_recombine(tournament_amount,(60,k))
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(crossover_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Mutation Percent: {}'.format(i*2) for i in range(mut_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Microbial GA Optimization, Number of Climbers: 10')
plt.show()

#Checking for optimal mutation Rate high climbers
generations = 1000
climbers = 100
hco1 = HillClimbers(climbers,items,max_vol)
mut_tests = 5

mut_tests = [[] for x in range(mut_tests)]
for k in range(crossover_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.tournament_recombine(tournament_amount,(60,k))
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(mut_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Mutation Percent: {}'.format(i*2) for i in range(mut_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Microbial GA Optimization, Number of Climbers: 100')
plt.show()









#checking for low climber Rate
generations = 1000
climbers = 10
hco1 = HillClimbers(climbers,items,max_vol)
crossover_tests = 5

mut_tests = [[] for x in range(crossover_tests)]
for k in range(crossover_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.tournament_recombine(tournament_amount,((k+1)*20),pMutate)
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(crossover_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Crossover Probability: {}'.format((i+1)*20) for i in range(crossover_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Microbial GA Optimization, Number of Climbers: 10')


#checking for high climber Rate
generations = 1000
climbers = 10
hco1 = HillClimbers(climbers,items,max_vol)
crossover_tests = 5

mut_tests = [[] for x in range(crossover_tests)]
for k in range(crossover_tests):
    hco = copy.deepcopy(hco1)
    for i in range(generations):
        hco.tournament_recombine(tournament_amount,((k+1)*20),pMutate)
        mut_tests[k].append(hco.max_fit())
data = [tuple(mut_tests[i][k] for i in range(crossover_tests))  for k in range(len(mut_tests[0]))]
ax2= pd.DataFrame(data,columns = ['Crossover Probability: {}'.format((i+1)*20) for i in range(crossover_tests)]).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('10 Climbers, 1000 Generations')
ax.plot()
plt.suptitle('Microbial GA Optimization, Number of Climbers: 100')
plt.show()
