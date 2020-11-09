import numpy as np
import random
import simple_agent

class MicrobialPhototaxis:
    microbes = None        #where the microbes are stored
    geno_size = 6          #size of the genotype, needs 6 for the simulated bot
    mutation_rate = 8/100  #1 percent of the genes range


    def __init__(self,N_microbes):
        self.microbes = np.random.uniform(low = -4,high = 4,size = (N_microbes,self.geno_size))
        #for gen in self.microbes:###-------------------------------------------------------------------------------------------------------one eyed
            #gen[1] = 0###-------------------------------------------------------------------------------------------------------one eyed
            #gen[3] = 0###-------------------------------------------------------------------------------------------------------one eyed

    #Takes a microbe and returns amutated one
    def mutate(self, geno):
        new_geno = geno
        for i in range(len(geno)):#iterates through each gene
            new_geno[i] = geno[i] + random.uniform(-self.mutation_rate,self.mutation_rate)#mutates gene by mutation rate(1%)
            if(new_geno[i] > 4):#wraparound
                new_geno[i] = new_geno[i] - 8
            if(new_geno[i] < -4):#wraparound
                new_geno[i] = new_geno[i] + 8
            #new_geno[1] = 0###-------------------------------------------------------------------------------------------------------one eyed
            #new_geno[3] = 0###-------------------------------------------------------------------------------------------------------one eyed
        return new_geno

    #takes a microbe with starting variable and returns  its fitness
    def fitness(self,geno,T = 150, initial_pos = [3,3],initial_degrees = 90):
        out  = simple_agent.run(T,initial_pos,initial_degrees,geno,0)
        #distance = (out[1][len(out[1])-1:] * out[1][len(out[1])-1:] ) + (out[0][len(out[0])-1:] * out[0][len(out[0])-1:] )
        y_dist = out[1][len(out[1])-1:]
        x_dist = out[0][len(out[0])-1:]

        return -((y_dist*y_dist)+(x_dist*x_dist))

    #2 microbes are tested against eachother , returns 1 if the first microbe wins and 2 if the second wins
    def compete(self, microbe1,microbe2, competitions = 5):
        mic_1_wins = 0
        mic_2_wins = 0
        for i in range(competitions):
            pos = [random.randint(1,10),random.randint(1,10)]
            degrees = random.randint(0,360)

            if (self.fitness(microbe1, initial_pos = pos, initial_degrees = degrees) >= self.fitness(microbe2,initial_pos = pos, initial_degrees = degrees)):
                mic_1_wins +=1
            else:
                mic_2_wins +=1
        if mic_1_wins > mic_2_wins:
            return 1##1wins
        else:
            return 2#returns 2wins

    #performes a tournament between all the microbes
    def tournament(self):
        amount = (int(len(self.microbes)/2))
        for i in range(amount):
            contestant1 = random.randint(0,len(self.microbes)-1)
            contestant2 = random.randint(0,len(self.microbes)-1)
            if contestant1 != contestant2:
                participant1 = self.microbes[contestant1]
                participant2 = self.microbes[contestant2]
                winner = self.compete(participant1,participant2)
                if winner == 1:
                    self.microbes[contestant2] =self.recombine(participant1,participant2)
                    self.microbes[contestant2] = self.mutate(self.microbes[contestant2])
                else:
                    self.microbes[contestant1] = self.recombine(participant2,participant1)
                    self.microbes[contestant1] = self.mutate(self.microbes[contestant1])

    def recombine(self,parent,child, pCrossover = 50):
        new_geno = child
        for i in range(len(parent)):
            if pCrossover > random.randint(0,101):
                new_geno[i] = parent[i]
        return new_geno

    def best_fitness(self):
        current = self.microbes[0]
        for mic in self.microbes:
            if (self.compete(mic,current)) == 1:
                current = mic
        return current

    def display_best(self,T = 150, initial_pos = [3,3],initial_degrees = 90):
        out  = simple_agent.run(T,initial_pos,initial_degrees,self.best_fitness(),1)


#Runs the algorithm
microbes = MicrobialPhototaxis(30)#initialise population
for x in range(200):#iterates through generations
    microbes.tournament()#performs a tournament each generation
print(microbes.fitness(microbes.best_fitness()))#prints the best fitness
print(microbes.best_fitness())#prints the best geno
microbes.display_best()#displays the best genos path
