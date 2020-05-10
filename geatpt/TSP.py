import numpy as np
import geatpy
import matplotlib.pyplot as plt

class TSP(geatpy.Problem):
    def __init__(self):
        name = "TSP"
        M = 1#优化的目标数
        maxormins = [1]#标记为求目标最小值
        Dim = 9#途经的路径数
        varTypes = [1]#标记变量类型，1代表离散
        lb = [1] * Dim # 决策变量下界
        ub = [9] * Dim # 决策变量上界
        lbin = [1] * Dim # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法
        geatpy.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        self.cities = np.random.randint(0,1000,size=(10,2))

    def aimFuc(self,pop): #实现目标函数
        mat = pop.Phen # 决策变量矩阵
        # 添加从0地出发且最后回到出发地
        X = np.hstack([np.zeros((mat.shape[0], 1)), mat, np.zeros((mat.shape[0], 1))]).astype(int)
        
        ObjV = [] # 存储所有种群个体对应的总路程
        for i in range(X.shape[0]):
            journey = self.places[X[i], :] # 按既定顺序到达的地点坐标
            distance = np.sum(np.sqrt(np.sum(np.diff(journey.T)**2, 0))) # 计算总路程
            ObjV.append(distance)
        pop.ObjV = np.array([ObjV]).T # 把求得的目标函数值赋值给种群pop的ObjV
        # 找到违反约束条件的个体在种群中的索引，保存在向量exIdx中（如：若0、2、4号个体违反约束条件，则编程找出他们来）
        exIdx1 = np.where(np.where(mat == 3)[1] - np.where(mat == 6)[1] < 0)[0]
        exIdx2 = np.where(np.where(mat == 4)[1] - np.where(mat == 5)[1] < 0)[0]
        exIdx = np.unique(np.hstack([exIdx1, exIdx2]))
        pop.CV = np.zeros((pop.sizes, 1))
        pop.CV[exIdx] = 1 # 把求得的违反约束程度矩阵赋值给种群pop的CV