def matrix_chain(p):
    """
    矩阵连乘问题
    :return:
    """
    _len_p = len(p)
    # 初始化动态规划数组(最小乘次数)
    dp = [[0 for j in range(_len_p - 1)] for i in range(_len_p - 1)]
    # 最优位置断开数组(最小乘次数时的断开点)
    s = [[0 for j in range(_len_p - 1)] for i in range(_len_p - 1)]
    # r为连乘矩阵的个数(i和j的间隔，从1开始)
    for r in range(1, _len_p):
        # i表示连乘矩阵中的第一个
        for i in range(_len_p - 1 - r):
            # j表示连乘矩阵中的最后一个(i+间隔)
            j = i + r
            # 计算出连乘次数
            dp[i][j] = dp[i][j] + dp[i + 1][j] + p[i] * p[i + 1] * p[j + 1]
            # 当前间断点为i
            s[i][j] = i
            # 在第一个和最后一个之间寻找断开点
            for k in range(i + 1, j):
                # 取到了间断点k
                t = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                # 更优解
                if t < dp[i][j]:
                    # 更新
                    dp[i][j] = t
                    s[i][j] = k
    return dp, s


if __name__ == '__main__':
    # A1 30*35 A2 35*15 A3 15*5 A4 5*10 A5 10*20 A6 20*25
    dp, s = matrix_chain([30, 35, 15, 5, 10, 20, 25])
    for dd in dp:
        print(dd)
    print()
    for dd in s:
        print(dd)
