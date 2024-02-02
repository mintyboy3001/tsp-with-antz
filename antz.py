
import numpy as np
import random

class graph:
    
    def __init__(self, size = 30):

        pairs = []
        
        for i in range(size):
            pair = (np.random.randint(100, 1100), np.random.randint(100, 800))
            pairs.append(pair)


        self.coords = np.asarray(pairs)
        self.size = len(self.coords)
        self.dists = np.zeros(self.size**2).reshape((self.size,self.size))

        for i in range(self.size):
            for j in range(i,self.size):
                self.dists[i][j] = np.linalg.norm(self.coords[i] - self.coords[j])
                self.dists[j][i] = np.linalg.norm(self.coords[i] - self.coords[j])
        
        prob = 0.999
        self.pheromones = (np.ones(self.size**2) * prob).reshape((self.size,self.size))
        for i in range(self.size):
            self.pheromones[i][i] = 0

    def scalar(self,m,n):
        min = 2**32-1
        max = -1
        for i in range(self.size):
            for j in range(i+1,self.size):
                if min > self.pheromones[i][j]:
                    min = self.pheromones[i][j]
                
                
                if max < self.pheromones[i][j]:
                    max = self.pheromones[i][j]
        try:
            return (self.pheromones[m][n] - min )/ (max - min)
        except:
            return 0
        
   

class ant:

    def __init__(self, grf: graph):
        self.q0 = 0
        self.beta = 1
        self.alpha = 0.10

        self.size = grf.size
        self.grf = grf

        self.memory = set(np.arange(grf.size))
        self.pos = np.random.choice(list(self.memory))
        self.start = self.pos
        self.memory.remove(self.pos)
        self.paths = np.ones(grf.size) * -1

        self.tourlen = 0


    def make_choice(self):
        
        sum = 0
        for a in self.memory:
            sum += self.grf.pheromones[self.pos][a] * (1/self.grf.dists[self.pos][a])**1.5
        
        
        probs = []
        
        for a in self.memory:
            val = self.grf.pheromones[self.pos][a] * (1/self.grf.dists[self.pos][a])**1.5
            probs.append( val / sum)

        try:
            return random.choices(list(self.memory), weights = probs, k =1)
        except:
            return random.choices(list(self.memory), weights = probs, k =1 )
            

    def step(self):
        tau0 = 0.08

        i = self.pos
        j = self.start

        if len(self.memory) > 0:

            next = self.make_choice()[0]

            self.paths[self.pos] = next
            self.tourlen += self.grf.dists[self.pos][next]
            
            self.pos = next
            self.memory.remove(self.pos)



             ###implement local update
            self.grf.pheromones[i][j] = (1-self.alpha) * self.grf.pheromones[i][j] + self.alpha * tau0
            self.grf.pheromones[j][i] = self.grf.pheromones[i][j]

            return -1
        else:
            self.paths[self.pos] = self.start
            self.tourlen += self.grf.dists[self.pos][self.start]

            
            self.grf.pheromones[i][j] = (1-self.alpha) * self.grf.pheromones[i][j] + self.alpha * tau0
            self.grf.pheromones[j][i] = self.grf.pheromones[i][j]

            return 1
    
    def reset(self):
        self.memory = set(np.arange(self.size))
        self.pos = np.random.choice(list(self.memory))
        self.start = self.pos
        self.memory.remove(self.pos)
        self.paths = np.ones(self.size) * -1
        self.tourlen = 0

    def normalize(self):

        
        sum = np.sum(self.grf.pheromones, axis = 1)
        for j in range(self.size):
            self.grf.pheromones[j] = 2* self.grf.pheromones[j] / sum[j]
        for i in range(self.size):
            self.grf.pheromones[i][i] = 0

        return
    



    

class colony:

    def __init__(self, grf: graph , n:int = 10 ):
        self.register = []
        for _ in range(n):
            self.register.append(ant(grf))
        self.tourlen = -1

    def step(self):

        for ant in self.register:
            ant.step()

    def reset(self):
        for ant in self.register:
            ant.reset()
        
        self.register[0].normalize()

    def update(self):
        
        min = 2**32-1
        grf = self.register[0].grf

        for idx, ant in enumerate(self.register):

            if min >= ant.tourlen:
                min = ant.tourlen
            diff = min - ant.tourlen + 0.005
            w = 0.01/diff
            for i,j in enumerate(self.register[idx].paths):
                j = int(j)
                grf.pheromones[i][j] += w 
                grf.pheromones[j][i] += w 
            self.tourlen = min
        
        
             

            

     