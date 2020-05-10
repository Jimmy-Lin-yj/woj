import numpy as np
import matplotlib.pyplot as plt

class TSP():
    def __init__(self, n_cities):
        self.city_position = np.random.rand(n_cities, 2)#生成所有城市的坐标
        plt.ion()#打开交互模式

    def plotting(self, lx, ly, total_d):
        plt.cla()
        #清除当前坐标轴
        plt.scatter(self.city_position[:, 0].T, self.city_position[:, 1].T, s=100, c='k')
        #绘制散点图，c='k'颜色为黑色
        plt.plot(lx.T, ly.T, 'r-')
        #lx.T表示对数组矩阵进行转置，plot进行划线
        plt.text(-0.05, -0.05, "Total distance=%.2f" % total_d, fontdict={'size': 20, 'color': 'red'})
        #在指定坐标处放置文本对象
        plt.xlim((-0.1, 1.1))
        plt.ylim((-0.1, 1.1))#设置坐标轴范围
        plt.pause(0.01)      #暂停进行刷新
        #plt.title("TSP实例")
        #plt.legend给线做标记
