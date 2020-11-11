from random import randint, random

def eqpFitness(position):
    if position == None:
        return 999
    fitness = 0
    for j1 in range(len(position)):
        for j2 in range(j1+1, len(position)):
            if (position[j1] == position[j2]):
                fitness += 1
            elif (position[j1] + j1 == position[j2] + j2 or
            position[j1] - j1 == position[j2] - j2):
                fitness += 1
    return fitness

class Particle:
    def __init__(self, v_max):
        #temp = [0,1,2,3,4,5,6,7]
        self.position = []
        self.velocity = []
        for i in range(8):
            #x = randint(0,len(temp)-1)
            #self.position.append(temp[x])
            self.position.append(randint(0,7))
            #del temp[x]
            self.velocity.append(randint(-v_max, v_max))
        self.p = self.position.copy()

class PSO:
    def __init__(self, v_max, omega, c_1, c_2, S):
        self.v_max = v_max
        self.omega = omega
        self.c_1 = c_1
        self.c_2 = c_2
        self.S = S
        self.swarm = []        
        for i in range(S):
            self.swarm.append(Particle(v_max))
        self.best_generation = None
        self.best_global = self.swarm[0].position
        for i in range(S):
            if (eqpFitness(self.swarm[i].position) < eqpFitness(self.best_global)):
                self.best_global = self.swarm[i].position.copy()
        self.max_generations = 300

    def search(self):
        print("\nBEGINNING SEARCH...")
        for generation in range(self.max_generations):
            print("\nGeneration " + str(generation) + ": ")
            self.best_generation = None
            for i in range(len(self.swarm)):
                phi_1 = random()
                phi_2 = random()
                
                # evaluate fitness
                particle_fitness_temp = eqpFitness(self.swarm[i].position)
                # update p
                if (particle_fitness_temp <= eqpFitness(self.swarm[i].p)):
                    self.swarm[i].p = self.swarm[i].position.copy()
                # update best_iteration
                if (particle_fitness_temp <= eqpFitness(self.best_generation)):
                    self.best_iteration = self.swarm[i].position.copy()
                # update best_global
                if (particle_fitness_temp <= eqpFitness(self.best_global)):
                    self.best_global = self.swarm[i].position.copy()

                # adapt velocity
                #print(self.swarm[i].velocity)
                temp_1 = [self.omega*x for x in self.swarm[i].velocity] 
                temp_2 = [self.c_1*phi_1*x for x in [x-y for x, y in zip(self.swarm[i].p, self.swarm[i].position)]]
                temp_3 = [self.c_2*phi_2*x for x in [x-y for x, y in zip(self.best_global, self.swarm[i].position)]]
                self.swarm[i].velocity = [x+y+z for x, y, z in zip(temp_1, temp_2, temp_3)]
                for j in range(8):
                    if (self.swarm[i].velocity[j] < -self.v_max):
                        self.swarm[i].velocity[j] = -self.v_max
                    elif (self.swarm[i].velocity[j] > self.v_max):
                        self.swarm[i].velocity[j] = self.v_max
                    else:
                        self.swarm[i].velocity[j] = round(self.swarm[i].velocity[j])
                #print(self.swarm[i].velocity)
                # update position
                #print(self.swarm[i].position)
                self.swarm[i].position = [x+y for x, y in zip(self.swarm[i].position, self.swarm[i].velocity)]
                for j in range(8):
                    if (self.swarm[i].position[j] < 0):
                        self.swarm[i].position[j] = 0
                    elif (self.swarm[i].position[j] > 7):
                        self.swarm[i].position[j] = 7
                #print(self.swarm[i].position)

                
                
                # break the search
                if (eqpFitness(self.best_global) == 0):
                    print("\nSOLUTION FOUND:")
                    print("Solution / Fitness: " + str(self.best_global) + " / " + str(eqpFitness(self.best_global)))
                    return 0

                
            
            #for elem in self.swarm:
            #        print(elem.position)

            
            print("Best iteration: " + str(self.best_iteration))
            print("Best iteration fitness: " + str(eqpFitness(self.best_iteration)))
            print("Best global: " + str(self.best_global))
            print("Best global fitness: " + str(eqpFitness(self.best_global)))
        return str(eqpFitness(self.best_global))

