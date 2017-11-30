def greedy_selector(_ls):
    """
    贪心选择
    活动安排问题
    :param _ls: 活动信息[(start1,end1),(s..,e..),...],并且是已经按照结束时间的非减顺序排列
    :return: 按顺序表示每个活动是否选择
    """
    _count = len(_ls)  # 活动总数
    _res = [0] * _count
    _res[0] = 1  # 第一个活动默认选中
    _end = _ls[0][1]  # 记录第一个活动的结束时间(最近一个被选中的活动的结束时间)
    for i in range(1, _count):
        if _ls[i][0] >= _end:  # _ls[i][0]第i个活动的开始时间
            _res[i] = 1
            _end = _ls[i][1]  # 新的被选中的活动，记录下来结束时间
    return _res


if __name__ == '__main__':
    # 测试数据，活动列表
    event_list = [
        (1, 4), (3, 5),
        (0, 6), (5, 7),
        (3, 8), (5, 9),
        (6, 10), (8, 11),
        (8, 12), (2, 13),
        (12, 14)
    ]
    print(greedy_selector(event_list))
