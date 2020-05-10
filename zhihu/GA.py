#from zhihu.population import population
import numpy as np
class GA():
    def __init__(self,DNA_size,pcross,pmutation,pop_size):
        self.DNA_size = DNA_size
        self.pcross = pcross
        self.pmutation = pmutation
        self.pop_size = pop_size
        self.pop = np.vstack([np.random.permutation(DNA_size) for i in range(pop_size)])
        #self.pop = population(DNA_size,pcross,pmutation,0,pop_size)
        #self.pop.individuals = np.vstack([np.random.permutation(DNA_size) for i in range(pop_size)])
        #生成一个随机种群

    #顺序获取城市的坐标，DNA为一个种群的基因
    def translateDNA(self,DNA,city_position):
        line_x = np.empty_like(DNA, dtype=np.float64)
        line_y = np.empty_like(DNA, dtype=np.float64)
        #生成与原数组形状相同的数组
        for i, d in enumerate(DNA):
            city_coord = city_position[d]
            line_x[i, :] = city_coord[:, 0]#line_x[i,:]代表第i行所有元素，后者代表所有行第一个元素
            line_y[i, :] = city_coord[:, 1]
        return line_x, line_y

    def get_fitness(self,line_x,line_y):
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)
        #shape属性为数组各个维度的维数
        for i, (xs, ys) in enumerate(zip(line_x, line_y)):
            total_distance[i] = np.sum(np.sqrt(np.square(np.diff(xs)) + np.square(np.diff(ys))))
            #计算种群中每条路径的长度,xs为所有要计算的路径的横坐标的集合
            #diff函数计算每一维的离散差值，也就是后一个元素减去前一个元素
        fitness = np.exp(self.DNA_size * 2 / total_distance)
        #np.exp()返回e的幂次方
        return fitness, total_distance

    def select(self,fitness):
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness / fitness.sum())
        #从range(popsize)中根据适应度作为概率，随机挑选满足种群数量的下一代种群
        return self.pop[idx]
        #array数组可以使用一个数组作为索引

    def crossover(self,parent,pop):
        #根据随机产生的概率决定是否进行交叉
        if np.random.rand() < self.pcross:
            i_ = np.random.randint(0, self.pop_size, size=1)   # 从种群中挑选一个个体
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)   
            # 选择交叉点，astype进行数据类型转换
            keep_city = parent[~cross_points]                                       
            # find the city number，~取反，parent是一个父代个体，为true则选中
            swap_city = pop[i_, np.isin(pop[i_].ravel(), keep_city, invert=True)]
            #np.isin测试所求数组中的元素是否在另一个数组中存在，返回与元素相同的bool型数组
            #ravel 将多维数组降为一维，
            parent[:] = np.concatenate((keep_city, swap_city))
            #将两个数组进行拼接
        return parent

    def mutate(self,child):
        for point in range(self.DNA_size):
            if np.random.rand() < self.pmutation:
                swap_point = np.random.randint(0, self.DNA_size)
                swapA, swapB = child[point], child[swap_point]#child为子代个体
                child[point], child[swap_point] = swapB, swapA
        return child

    def evolve(self,fitness):
        pop = self.select(fitness)
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop