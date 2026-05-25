"""
================================================================================
模拟退火算法（Simulated Annealing, SA）求解旅行商问题（TSP）
================================================================================

【文件依赖关系】
    - 本文件为单文件实现，无跨文件依赖
    - 依赖 data/st70.tsp 数据集文件（TSPLIB 标准格式）
    - 依赖的第三方库：numpy, matplotlib

【算法整体流程（8 步）】
    1. 读取 TSP 数据文件，解析城市坐标矩阵
    2. 初始化超参数（初始温度 T0、终止温度 Tend、降温系数 rate、种群大小 size）
    3. 计算城市间距离矩阵（对角线设为 inf，防止路径自环）
    4. 初始化一条随机路径作为当前解
    5. 在当前温度下，通过"片段逆转"策略生成新解
    6. 根据 Metropolis 准则（以概率 exp(-ΔE/T) 接受差解）判断是否接受新解
    7. 在当前温度下重复步骤 5-6 共 size 次，选出种群中最优解并更新全局最优
    8. 降温 (T = T * rate)，重复步骤 5-7 直到温度低于终止温度

【关于算法设计的特殊说明】
    本实现中，`sa()` 方法在每次降温前会生成 size=100 个新解组成"种群"，
    然后从种群中选出最优路径。这不是标准 SA 的做法（标准 SA 每次温度
    只维护一个解并做多次扰动），而是结合了"种群搜索"思想的混合设计。
    这种设计的好处是：在每一温度下探索更广的解空间，降低了对初始解的依赖。
    代价是：每轮的计算复杂度为 O(size × num_city)，比标准 SA 高 size 倍。

【全局变量/实例变量一览】
    T0         : float   - 当前温度（在外循环中递减）
    Tend       : float   - 终止温度阈值
    rate       : float   - 降温系数（0.94，即每轮温度降为原来的 94%）
    size       : int     - 种群大小（每个温度下产生的候选解数量）
    num_city   : int     - 城市数量
    location   : ndarray - 城市坐标矩阵，shape=(num_city, 2)
    dis_mat    : ndarray - 城市间距离矩阵，shape=(num_city, num_city)，对角线为 inf
    fire       : list    - 当前解（城市下标列表，表示访问顺序）
    fires      : list    - 弃用的实例变量（原本用于存储种群，现已内联到 sa() 中）
    iter_x     : list    - 收敛图 x 轴（迭代次数）
    iter_y     : list    - 收敛图 y 轴（每轮最优路径长度）

参考来源：https://github.com/chris-tao/TSP_collection
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt


class SA(object):
    """
    模拟退火算法求解器

    【功能】
        使用模拟退火算法求解旅行商问题（TSP），寻找访问所有城市恰好一次
        并返回起点（Hamilton 回路）的最短路径。

    【超参数】
        T0   = 2000    - 初始温度（较高温度有利于在初期充分探索解空间）
        Tend = 1e-3    - 终止温度（温度低于此值时算法终止）
        rate = 0.94    - 降温系数（每轮温度乘以此系数，典型值 0.85~0.99）
        size = 100     - 种群大小（每个温度下生成候选解的数量）
    """

    def __init__(self, num_city, data):
        """
        【函数名】__init__
        【功能】初始化模拟退火求解器，完成数据准备、参数设置和初始解生成

        【运作流程】
            1. 存储城市数量 num_city 和城市坐标 data
            2. 设置超参数：T0=2000, Tend=1e-3, rate=0.94, size=100
            3. 计算距离矩阵 dis_mat（调用 compute_dis_mat）
            4. 生成初始随机路径 fire（调用 random_init）
            5. 初始化 fires 列表（虽然后续未使用，保留以兼容旧代码）
            6. 初始化 scores 列表（预留的评分容器，当前未使用）
            7. 计算初始路径长度，绘制"初始最优路径"子图
            8. 初始化收敛曲线数据 iter_x, iter_y

        【重要实例变量（全局视角）】
            self.T0        : float     - 当前温度（会随退火过程递减）
            self.Tend      : float     - 终止温度，算法停止条件
            self.rate      : float     - 降温倍率，每次降温：T_new = T_old * rate
            self.size      : int       - 每轮生成的候选解数量
            self.num_city  : int       - 城市总数
            self.location  : ndarray   - 城市坐标，shape=(num_city, 2)
            self.dis_mat   : ndarray   - 距离矩阵，shape=(num_city, num_city)
                                        对角线为 inf，防止路径自环
            self.fire      : list[int] - 当前解（城市访问顺序），是算法的核心状态变量
            self.fires     : list      - 弃用变量（原本用于存储多路径，现已内联）
            self.scores    : list      - 预留变量，当前未使用
            self.iter_x    : list[int] - 收敛图横轴：迭代轮次
            self.iter_y    : list[float] - 收敛图纵轴：对应轮次的最优路径长度

        【依赖的子函数】
            - self.random_init(num_city)      : 生成随机初始路径
            - self.compute_dis_mat(num_city, data) : 计算距离矩阵
            - self.compute_pathlen(path, dis_mat)  : 计算路径长度（间接调用）
        """
        self.T0 = 2000
        self.Tend = 1e-3
        self.rate = 0.94
        self.size = 100
        self.num_city = num_city
        self.scores = []          # 预留变量（当前未使用）
        self.location = data
        self.fire = self.random_init(num_city)
        self.fires = []           # 弃用变量（保留兼容）
        self.dis_mat = self.compute_dis_mat(num_city, data)

        # 绘制初始随机路径
        init_pathlen = 1. / self.compute_pathlen(self.fire, self.dis_mat)
        init_best = self.location[self.fire]
        init_best = np.vstack((init_best, init_best[0]))
        plt.subplot(2, 2, 2)
        plt.title('init best result')
        plt.plot(init_best[:, 0], init_best[:, 1])

        # 初始化收敛曲线数据
        self.iter_x = [0]
        self.iter_y = [1. / init_pathlen]

    def random_init(self, num_city):
        """
        【函数名】random_init
        【功能】生成一个随机的城市访问顺序作为初始解

        【运作流程】
            1. 创建列表 [0, 1, 2, ..., num_city-1]（所有城市下标）
            2. 使用 random.shuffle 随机打乱顺序
            3. 返回打乱后的列表作为初始路径

        【局部变量说明】
            - tmp (list[int]): 城市下标列表，生成后打乱返回
            - num_city (int): 函数入参，城市总数

        【依赖关系】
            无依赖（不调用任何其他函数，不访问实例变量）

        【输入】
            num_city (int): 城市总数

        【输出】
            list[int]: 随机排列的城市下标列表
        """
        tmp = [x for x in range(num_city)]
        random.shuffle(tmp)
        return tmp

    def compute_dis_mat(self, num_city, location):
        """
        【函数名】compute_dis_mat
        【功能】计算所有城市两两之间的欧氏距离，构建距离矩阵

        【运作流程】
            1. 创建 num_city × num_city 的零矩阵 dis_mat
            2. 双重循环遍历所有城市对 (i, j)：
               a. 若 i == j（同一城市），设 dis_mat[i][j] = inf（避免路径自环）
               b. 否则，取城市 i 和城市 j 的坐标 (x_i, y_i) 和 (x_j, y_j)
               c. 计算欧氏距离：d = sqrt((x_i-x_j)² + (y_i-y_j)²)
               d. 存入 dis_mat[i][j]
            3. 返回填充完整的距离矩阵

        【关键设计说明】
            对角线设为 np.inf（无穷大）而非 0，是为了在 compute_pathlen 中
            计算路径总长度时，如果某段路径意外地"从一个城市到它自己"，
            该段距离为 ∞，从而该路径不会被选为最优解。这是一种防御性编程。

        【局部变量说明】
            - dis_mat (ndarray): shape=(num_city, num_city)，距离矩阵
            - a (ndarray): 城市 i 的坐标 [x, y]
            - b (ndarray): 城市 j 的坐标 [x, y]
            - tmp (float): 城市 i 和 j 之间的欧氏距离

        【依赖关系】
            不依赖其他实例方法，仅使用入参 location 和 num_city

        【输入】
            num_city (int): 城市总数
            location (ndarray): 城市坐标，shape=(num_city, 2)

        【输出】
            ndarray: 距离矩阵，shape=(num_city, num_city)
        """
        dis_mat = np.zeros((num_city, num_city))
        for i in range(num_city):
            for j in range(num_city):
                if i == j:
                    dis_mat[i][j] = np.inf   # 自己到自己的距离设为 ∞，防止自环
                    continue
                a = location[i]
                b = location[j]
                tmp = np.sqrt(sum([(x[0] - x[1]) ** 2 for x in zip(a, b)]))
                dis_mat[i][j] = tmp
        return dis_mat

    def compute_pathlen(self, path, dis_mat):
        """
        【函数名】compute_pathlen
        【功能】计算一条完整 Hamilton 回路的总长度

        【运作流程】
            1. 取路径首尾城市 a = path[0], b = path[-1]
            2. 初始总长度 = dis_mat[a][b]（回路闭合段：从最后一个城市回到起点）
            3. 遍历路径中相邻城市对 (path[i], path[i+1])：
               累加 dis_mat[path[i]][path[i+1]]
            4. 返回总长度

        【哈密顿回路说明】
            TSP 要求从起点出发，访问所有城市各一次，最后返回起点。
            因此路径总长度 = 所有相邻城市段之和 + 首尾闭合段。

        【局部变量说明】
            - a (int): 当前段的起始城市下标
            - b (int): 当前段的目标城市下标
            - result (float): 累计路径长度

        【依赖关系】
            依赖入参 dis_mat（距离矩阵），不修改任何实例变量

        【输入】
            path (list[int]): 城市访问顺序列表
            dis_mat (ndarray): 距离矩阵

        【输出】
            float: 路径总长度
        """
        a = path[0]
        b = path[-1]
        result = dis_mat[a][b]       # 闭合段：从最后一个城市回到起点
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            result += dis_mat[a][b]
        return result

    def compute_paths(self, paths):
        """
        【函数名】compute_paths
        【功能】批量计算种群中所有路径的长度

        【运作流程】
            1. 创建空列表 result
            2. 遍历 paths 中的每条路径 one：
               a. 调用 self.compute_pathlen(one, self.dis_mat) 计算路径长度
               b. 将长度追加到 result
            3. 返回长度列表

        【局部变量说明】
            - result (list[float]): 每条路径的长度列表
            - one (list[int]): 种群中的单条路径
            - length (float): 单条路径的长度

        【依赖的子函数】
            - self.compute_pathlen(path, dis_mat): 计算单条路径长度

        【输入】
            paths (list[list[int]]): 多条路径的列表

        【输出】
            list[float]: 对应每条路径的长度
        """
        result = []
        for one in paths:
            length = self.compute_pathlen(one, self.dis_mat)
            result.append(length)
        return result

    def get_new_fire(self, fire):
        """
        【函数名】get_new_fire
        【功能】对当前路径施加"片段逆转"扰动，生成邻域新解

        【运作流程】
            1. 随机选择路径中的两个位置 a 和 b
            2. 取较小的位置 x = min(a, b)，较大的位置 y = max(a, b)
            3. 将路径分为三段：
               - 前段 a_part = fire[:x]（保持原序）
               - 中段 b_part = fire[x:y]（逆序反转）
               - 后段 c_part = fire[y:]（保持原序）
            4. 拼接：a_part + b_part[::-1] + c_part，作为新路径返回

        【为什么选择"片段逆转"而非"两点交换"？】
            代码中保留了两种策略的注释：
            - 策略1（交换两个元素）：fire[a], fire[b] = fire[b], fire[a]
              效果较差，因为交换只改变了两个城市的顺序，邻域变化太小。
            - 策略2（片段逆转）：将一段子路径完全反转。
              效果更好，因为逆转一段路径能更大幅度改变解的结构，
              更容易跳出局部最优，同时仍保持了路径的"连续性"。

        【局部变量说明】
            - a, b (int): 随机选中的两个位置
            - x, y (int): x = min(a,b), y = max(a,b)，确定逆转片段的起止位置
            - a_part (list): fire[:x]，前段保持原序
            - b_part (list): fire[x:y][::-1]，中段逆序
            - c_part (list): fire[y:]，后段保持原序

        【依赖关系】
            不调用任何子函数或访问实例变量，仅依赖入参 fire

        【输入】
            fire (list[int]): 当前路径

        【输出】
            list[int]: 施加片段逆转后的新路径
        """
        t = [x for x in range(len(fire))]
        a, b = np.random.choice(t, 2)
        # 策略1（交换两个元素，效果较差，已弃用）：
        # fire[a], fire[b] = fire[b], fire[a]
        # 策略2（片段逆转，效果更好）：
        x = min(a, b)
        y = max(a, b)
        a_part = fire[:x]
        b_part = fire[x:y][::-1]   # 逆序反转中间片段
        c_part = fire[y:]
        return a_part + b_part + c_part

    def eval_fire(self, raw, get, temp):
        """
        【函数名】eval_fire
        【功能】根据 Metropolis 准则判断是否接受新解

        【运作流程】
        Metropolis 准则是模拟退火的核心机制，分为两种情况：
            情况 A（新解更优，ΔE < 0）：
                - 无条件接受新解，返回 get
            情况 B（新解更差，ΔE ≥ 0）：
                - 计算接受概率 P = exp(-ΔE / T)
                - 生成 [0, 1) 均匀随机数 r
                - 若 r ≤ P，接受新解（返回 get）
                - 否则拒绝新解（返回 raw）
        
        【为什么以概率 exp(-ΔE/T) 接受差解？】
            物理类比：固体退火中，粒子在温度 T 下具有能量 E 的概率正比于
            Boltzmann 因子 exp(-E/kT)。Metropolis 算法将其转化为：
            若新状态能量更高（ΔE > 0），以概率 exp(-ΔE/T) 接受该状态。
            
            在 TSP 中，ΔE = 新路径长度 - 旧路径长度。
            高温时（T 大），exp(-ΔE/T) ≈ 1，几乎接受所有新解 → 广泛探索。
            低温时（T 小），exp(-ΔE/T) ≈ 0，几乎只接受更优解 → 精细收敛。

        【概率下限保护（max(1e-4, ...)）】
            当 T 极低且 ΔE 很大时，exp(-ΔE/T) 可能趋近于 0（如 1e-300），
            此时算法几乎无法接受任何差解，容易陷入局部最优。
            设置概率下限 1e-4，相当于保留一条极小的"逃生通道"，
            使算法在极低温下仍有微小概率跳出局部最优。

        【局部变量说明】
            - len1 (float): 当前解 raw 的路径长度
            - len2 (float): 候选新解 get 的路径长度
            - dc (float): 能量差 ΔE = len2 - len1
                          负值 = 新解更优（无条件接受）
                          正值 = 新解更差（概率接受）
            - p (float): 接受概率 P = max(1e-4, exp(-dc/T))

        【依赖的子函数】
            - self.compute_pathlen(path, dis_mat): 计算路径长度
            - np.exp(): 指数函数 e^x
            - np.random.rand(): 生成 [0, 1) 随机数

        【与实例变量的关系】
            只读 self.dis_mat（距离矩阵），不修改任何实例变量

        【输入】
            raw (list[int]): 当前解
            get (list[int]): 候选新解
            temp (float): 当前温度 T

        【输出】
            list[int]: 经过 Metropolis 准则筛选后的解（可能是 raw 或 get）
        """
        len1 = self.compute_pathlen(raw, self.dis_mat)
        len2 = self.compute_pathlen(get, self.dis_mat)
        dc = len2 - len1                # ΔE = 路径变化量
        p = max(1e-4, np.exp(-dc / temp))  # 接受概率（防止概率过低）
        if len2 < len1:
            return get                  # 新解更优 → 无条件接受
        elif np.random.rand() <= p:
            return get                  # 条件接受差解
        else:
            return raw                  # 拒绝差解

    def sa(self):
        """
        【函数名】sa
        【功能】执行模拟退火主循环，寻找最短 Hamilton 回路

        【运作流程（详细）】
            1. 初始化：
               - count = 0（迭代轮次计数器）
               - best_path = self.fire（当前最优路径）
               - best_length = 初始路径长度
            
            2. 外循环（退火过程）：当 T0 > Tend 时持续执行
               a. count += 1
               b. 内循环（种群搜索）：重复 size 次
                  - 对 self.fire 的副本施加片段逆转扰动，得到 tmp_new
                  - 用 eval_fire 判断是否接受 tmp_new：
                    * 若接受：self.fire 更新为 tmp_new
                    * 若拒绝：self.fire 保持不变
                  - 将 tmp_new 加入临时种群 tmp_fires
               c. 从 tmp_fires 中选出长度最短的路径 min_path
               d. 若 min_path 长度 < best_length，更新全局最优解
               e. 降温：self.T0 *= self.rate
               f. 记录收敛数据到 self.iter_x 和 self.iter_y
            
            3. 循环结束，返回全局最优路径长度和路径

        【"种群+退火"混合设计说明】
            标准 SA 在固定温度下通常对一个解进行多次扰动并反复调用
            Metropolis 准则更新该解（马尔可夫链）。而本实现中：
            - 内循环生成 size=100 个新解构成"种群" tmp_fires
            - self.fire 在内循环中随接受/拒绝而演变（符合 SA）
            - 但最终从整批候选解中选出最优解（类似 GA 的精英选择）
            
            这种混合设计的优点：
            - 扩大了每轮对解空间的探索范围
            - 降低了对初始解的敏感度
            缺点：
            - 每轮计算复杂度 O(size × num_city)，比标准 SA 高约 size 倍
            - self.fire 在内循环中的演变过程被"浪费"（最终选的是种群最优，
              而非 self.fire 的最后状态）

        【关键变量追踪】
            【全局/实例变量】
            - self.T0 (float): 当前温度，从 2000 逐步降至 1e-3
            - self.fire (list): 当前解状态，在内循环中随接受/拒绝动态变化
            - self.iter_x (list): 每轮追加 count，记录迭代轮次
            - self.iter_y (list): 每轮追加 best_length，记录最优路径长度
            【局部变量】
            - count (int): 迭代轮次计数器（同时也是降温次数）
            - best_path (list): 全局最优路径（整个算法找到的最好解）
            - best_length (float): 全局最优路径长度
            - tmp_fires (list[list[int]]): 当前温度的候选解"种群"
            - lengths (list[float]): 种群中每条路径的长度
            - min_length (float): 当前种群中的最短长度
            - min_index (int): 最短路径在种群中的索引
            - min_path (list[int]): 当前种群中的最短路径

        【依赖的子函数】
            - self.get_new_fire(fire): 生成邻域新解
            - self.eval_fire(raw, get, temp): Metropolis 接受准则
            - self.compute_paths(paths): 批量计算路径长度

        【输入】
            无（所有参数从实例变量读取）

        【输出】
            tuple: (best_length, best_path)
                - best_length (float): 全局最优路径长度
                - best_path (list[int]): 全局最优路径（城市下标列表）
        """
        count = 0
        # 初始化全局最优解
        best_path = self.fire
        best_length = self.compute_pathlen(self.fire, self.dis_mat)

        while self.T0 > self.Tend:                     # 外循环：退火过程
            count += 1
            tmp_fires = []                              # 当前温度的候选解集合
            for _ in range(self.size):                  # 内循环：产生 size 个新解
                tmp_new = self.get_new_fire(self.fire.copy())  # 扰动生成新解
                self.fire = self.eval_fire(self.fire, tmp_new, self.T0)  # 退火判断
                tmp_fires.append(tmp_new)
            # 从种群中选出本轮最优解
            lengths = self.compute_paths(tmp_fires)
            min_length = min(lengths)
            min_index = lengths.index(min_length)
            min_path = tmp_fires[min_index]
            # 更新全局最优解
            if min_length < best_length:
                best_length = min_length
                best_path = min_path
            # 降温
            self.T0 *= self.rate
            # 记录收敛数据
            self.iter_x.append(count)
            self.iter_y.append(best_length)
        return best_length, best_path

    def run(self):
        """
        【函数名】run
        【功能】启动模拟退火求解，并绘制收敛曲线和最终路径

        【运作流程】
            1. 调用 self.sa() 执行核心退火算法，获得最优解
            2. 绘制收敛曲线子图（迭代次数 vs 最优路径长度）
            3. 返回最优路径坐标和长度，供外部绘图使用

        【依赖的子函数】
            - self.sa(): 模拟退火核心算法

        【输入】
            无

        【输出】
            tuple: (best_path_coords, best_length)
                - best_path_coords (ndarray): 最优路径的城市坐标序列，shape=(num_city, 2)
                - best_length (float): 最优路径的总长度
        """
        best_length, best_path = self.sa()
        # 绘制收敛曲线
        plt.subplot(2, 2, 4)
        plt.title('convergence curve')
        plt.plot(self.iter_x, self.iter_y)
        return self.location[best_path], best_length


# ============================================================================
# 数据读取函数（模块级函数，不属于 SA 类）
# ============================================================================

def read_tsp(path):
    """
    【函数名】read_tsp
    【功能】解析 TSPLIB 标准格式的 .tsp 文件，提取城市坐标

    【运作流程】
        1. 读取文件所有行
        2. 定位 'NODE_COORD_SECTION' 行（坐标数据起始标记）
        3. 从该行之后逐行解析：
           a. 过滤掉空行和 'EOF' 标记
           b. 每行格式：<城市编号> <x坐标> <y坐标>
           c. 提取 x 和 y 坐标为浮点数
        4. 返回坐标列表

    【局部变量说明】
        - lines (list[str]): 文件所有行
        - index (int): 'NODE_COORD_SECTION' 所在行号
        - data (list[str]): 坐标数据行（位于标记行之后、文件结束之前）
        - tmp (list): 最终坐标列表，元素为 [x, y]

    【依赖关系】
        无（独立函数，不依赖 SA 类或其他模块函数）

    【输入】
        path (str): .tsp 文件路径

    【输出】
        list[list[float]]: 城市坐标列表，每个元素为 [x坐标, y坐标]
    """
    lines = open(path, 'r').readlines()
    assert 'NODE_COORD_SECTION\n' in lines
    index = lines.index('NODE_COORD_SECTION\n')
    data = lines[index + 1:-1]
    tmp = []
    for line in data:
        line = line.strip().split(' ')
        if line[0] == 'EOF':
            continue
        tmpline = []
        for x in line:
            if x == '':
                continue
            else:
                tmpline.append(float(x))
        if tmpline == []:
            continue
        tmp.append(tmpline)
    data = tmp
    return data


# ============================================================================
# 主程序入口
# ============================================================================

if __name__ == '__main__':
    # 1. 读取 TSP 数据
    data = read_tsp('data/st70.tsp')
    data = np.array(data)
    plt.suptitle('SA in st70.tsp')
    data = data[:, 1:]                     # 去掉第一列（城市编号），保留 xy 坐标

    # 2. 绘制原始数据散点图
    plt.subplot(2, 2, 1)
    plt.title('raw data')
    show_data = np.vstack([data, data[0]]) # 将起点追加到末尾，形成闭合环（仅为显示）
    plt.plot(data[:, 0], data[:, 1])

    # 3. 多次运行取最优解
    Best, Best_path = math.inf, None
    foa = SA(num_city=data.shape[0], data=data.copy())
    path, path_len = foa.run()
    if path_len < Best:
        Best = path_len
        Best_path = path

    # 4. 绘制最优路径
    plt.subplot(2, 2, 3)
    Best_path = np.vstack([Best_path, Best_path[0]])  # 闭合回路
    plt.plot(Best_path[:, 0], Best_path[:, 1])
    plt.title('result')
    plt.show()