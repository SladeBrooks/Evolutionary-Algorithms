import numpy as np
import random
import copy
import pandas as pd
import matplotlib.pyplot as plt

class HillClimbers:
    climbers = None
    items = None
    max_vol = 0

    #creates hillclimbers saving them as a matrix with each row vector being a climber
    def __init__(self,N_climbers,items,max_vol):
        self.climbers = np.random.randint(low = 0,high = 2,size = (N_climbers,len(items)))
        self.items =items
        self.max_vol = max_vol

    """

    """
    def mutate_all(self,mut_rate = 1):
        for hc in self.climbers:
            #print('old gene: {}'.format(hc))
            after_mut = self.mutate(hc,mut_rate)
            for i in range(len(after_mut)):
                hc[i] = after_mut[i]
            #print('new gene: {}'.format(hc))
            #print(self.mutate(hc))

    """
    rec
    """
    def tournament_recombine(self,amount = 1, pCrossover = 1,pMutate = 1):
        for i in range(amount):
            part1key = random.randint(0,len(self.climbers)-1)
            part2key = random.randint(0,len(self.climbers)-1)
            if part1key != part2key:
                participant1 = self.climbers[part1key]
                participant2 = self.climbers[part2key]
                if self.fitness(participant1) >= self.fitness(participant2):
                    self.recombine(participant1,participant2,pCrossover,pMutate)
                else:
                    self.recombine(participant2,participant1,pCrossover,pMutate)



    """

    """
    def recombine(self,parent,child,pCrossover = 1,pMutate = 1):
        for i in range(len(parent)):
            if pCrossover > random.randint(0,101):
                child[i] = parent[i]
            if pMutate > random.randint(0,101):
                child[i] = 1-child[i]

        #return child

    """
        mutates a climber
        mut_rate: the number of genes to be flipped/mutated
        climber_vector: the vector for the climber to be mutated
        returns: either the mutated genes or the old genes, whichever has better fitness
    """
    def mutate(self,climber_vector, mut_rate):
        new_geno = [x for x in climber_vector]
        for i in range(len(new_geno)):
            mut_chance = random.randint(0,101)
            if mut_rate >=mut_chance:
                new_geno[i] = 1 - new_geno[i]
            #new_gen[random.randint(0,len(new_gen)-1)] = random.randint(0,1)
        #print('mutGen: {} oldGen: {}'.format(self.fitness(new_geno),self.fitness(climber_vector)))
        if self.fitness(new_geno) >= self.fitness(climber_vector):
            return new_geno
        else:
            return climber_vector

    #returns the fitness of a single climber, input is a climer vector
    def fitness(self,climber_vector):
        benefit = 0
        volume = 0
        for i in range(len(climber_vector)):
            if climber_vector[i] == 1:
                benefit = benefit + self.items[i][0]
                volume = volume + self.items[i][1]
        if volume > self.max_vol:
            return self.max_vol - volume
        else:
            return benefit



    def all_fitness(self):
        fit = []
        for hc in self.climbers:
            fit.append(self.fitness(hc))
        return fit

    def p(self):
        print(self.climbers)

    def max_fit(self):
        fitnesses = []
        for hc in self.climbers:
            fitnesses.append(self.fitness(hc))
        return max(fitnesses)
