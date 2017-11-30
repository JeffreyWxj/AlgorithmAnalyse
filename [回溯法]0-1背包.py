class Knapsack:
    def __init__(self, _ls, cc):
        """
        构造函数
        初始化成员变量
        计算平均价值
        :param _ls: [{weight:xxx,value:xxx,avg:xxx},...]
        :param cc: 背包容量
        """
        self.c = cc  # 背包容量
        self.n = len(_ls)  # 物品数目
        self.current_weight = 0  # 当前重量
        self.current_value = 0  # 当前价值
        self.best_value = 0  # 当前最优价值
        # 计算平均值
        for i in range(len(_ls)):
            item = _ls[i]
            item['avg'] = item['weight'] / item['value']
            _ls[i] = item
        # 排序
        sorted(_ls, key=lambda item: item['avg'])
        self.ls = _ls

    def knapsack(self):
        self.backtrack(0)
        return self.best_value

    def backtrack(self, i):
        if i >= self.n:
            self.best_value = max(self.current_value, self.best_value)
            return
        if self.current_weight + self.ls[i]['weight'] <= self.c:
            self.current_weight += self.ls[i]['weight']
            self.current_value += self.ls[i]['value']
            self.backtrack(i + 1)
            self.current_weight -= self.ls[i]['weight']
            self.current_value -= self.ls[i]['value']
        self.backtrack(i + 1)


if __name__ == '__main__':
    _list = [
        {'weight': 2, 'value': 6},
        {'weight': 2, 'value': 3},
        {'weight': 6, 'value': 5},
        {'weight': 5, 'value': 4},
        {'weight': 4, 'value': 6},
    ]
    ks = Knapsack(_list, 8)
    print(ks.knapsack())
