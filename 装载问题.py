class Loading():
    def __init__(self, box_weight_list, cc):
        self.box_weight_list = box_weight_list  # 集装箱重量列表
        self.n = len(box_weight_list) - 1  # 集装箱数目
        self.c = cc  # 第一艘轮船最大载重
        self.current_weight = 0  # 当前载重
        self.best_weight = 0  # 当前最优载重量

    def max_loading(self):
        # 从第0个开始装车，哦不，装船
        self.backtrack(0)
        # 上面递归结束之后，最优解就出来了，拿去吧
        return self.best_weight

    def backtrack(self, i):
        """
        回溯递归
        :return:
        """
        if i > self.n:
            # 这时候肯定已经超过叶节点啦，不能继续往下查了
            # 判断一下是不是最优解
            if self.current_weight > self.best_weight:
                self.best_weight = self.current_weight
            # 结束
            return
        # 还没到叶节点
        # 看一下加上下一个集装箱之后会不会超载
        if self.current_weight + self.box_weight_list[i] <= self.c:
            # 不超载就往上装
            self.current_weight += self.box_weight_list[i]
            # 装上之后继续看下一个能不能装(递归)
            self.backtrack(i + 1)
            # 上面的递归结束之后，把刚才装上去那个拿下来，去另一个分支继续查
            self.current_weight -= self.box_weight_list[i]
        self.backtrack(i + 1)


if __name__ == '__main__':
    # 测试数据，集装箱重量
    boxes = [1, 2, 3, 5, 6]
    # 实例化
    loading = Loading(boxes, 10)
    # 计算
    print(loading.max_loading())
