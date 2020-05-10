import matplotlib.pyplot as plt
import numpy as np
from GA import GA
from TSP import TSP

N_CITIES = 20  # DNA size
CROSS_RATE = 0.1
MUTATE_RATE = 0.02
POP_SIZE = 500
N_GENERATIONS = 500

ga = GA(DNA_size=N_CITIES, pcross=CROSS_RATE, pmutation=MUTATE_RATE, pop_size=POP_SIZE)
env = TSP(N_CITIES)
for gen in range(N_GENERATIONS):
    lx, ly = ga.translateDNA(ga.pop, env.city_position)
    fitness, total_distance = ga.get_fitness(lx, ly)
    ga.evolve(fitness)
    best_idx = np.argmax(fitness)#返回最大值的索引
    print('Gen:', gen, '| best fit: %.2f' % fitness[best_idx],)
    env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])
    #绘制出每一代的最优路径

plt.ioff()
plt.show()