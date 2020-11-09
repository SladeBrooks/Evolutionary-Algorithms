import numpy as np
import random
import copy
import pandas as pd
import matplotlib.pyplot as plt
from HillClimbers import HillClimbers

#Amount of climbers
climbers = 500
max_vol = 50
tournament_chance = 50 # hybrid: percent chance of a tournament occuring
tournament_amount = climbers#microbial: tournament amount is the number of tournaments in a microbial generation,currently set to the amount of climbers so 1 generation equals roughly a tournament for each climber
pCrossover = 50# microbial:pCrossover is the probability of recombining out of 100
pMutate = 2 #microbial:pMutate is percentage chance of mutation during gene crossover
mutation_rate = 2 #RMHC: mutation rate is the percentage chance of mutation


#The items for the knapsack, (benifit,volume)
items = [(6,10),(19,5),(7,15),(1,18),(13,1),(17,17),(3,12),(18,19),(16,16),(20,4),(5,9),(15,20),(12,13),(11,7),(9,3),(2,2),(14,6),(4,11),(10,8),(8,14)]
#B = [3,54,55,32,50,26,70,7,45,1,40,28,46,16,20,15,56,98,13,66,29,64,96,91,97,99,94,51,27,30,43,9,14,62,92,76,37,85,23,52,67,39,82,42,8,25,44,31,11,100,74,75,60,93,73,36,35,77,78,24,84,61,19,88,49,18,90,22,89,68,81,59,57,65,58,63,4,72,69,41,80,10,83,5,79,53,95,21,6,17,87,38,33,12,71,86,47,34,48,2]
#V = [6,8,5,10,8,6,7,14,11,9,14,6,12,12,10,6,10,7,6,7,13,5,7,5,9,5,13,6,5,8,9,6,14,8,7,5,7,5,10,12,11,5,5,12,14,10,6,13,8,7,12,5,5,11,11,10,12,12,12,7,11,10,8,5,12,8,11,12,6,6,10,9,13,12,12,5,5,5,12,14,11,6,12,6,6,11,8,11,12,10,12,7,12,14,13,5,8,8,11,10];
#items = [(B[i],V[i]) for i in range(len(B))]

generations = 1000

#create 3 origional sets all witht he same starting values
hc1 = HillClimbers(climbers,items,max_vol)#used as RMHC
hc2 = copy.deepcopy(hc1)#used as hybrid
hc3 = copy.deepcopy(hc1)#used for purely microbial GA

hc_stats = []
hb_stats = []
mc_stats = []

#RMHC
for i in range(generations):
    hc1.mutate_all(mutation_rate)
    hc_stats.append(hc1.max_fit())

for i in range(generations):
    hc2.tournament_recombine(tournament_amount,pCrossover,pMutate)
    mc_stats.append(hc2.max_fit())

for i in range(generations):
    if random.randint(0,101) > tournament_chance:
        hc3.mutate_all(mutation_rate)
    else:
        hc3.tournament_recombine(tournament_amount,pCrossover,pMutate)
    hb_stats.append(hc3.max_fit())

ax= pd.DataFrame([(hc_stats[i],hb_stats[i],mc_stats[i]) for i in range(len(hc_stats))],columns = ['RMHC', 'Hybrid','Microbial']).plot()
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.plot()
plt.suptitle('Comparison, climbers:{}'.format(climbers))
plt.show()
