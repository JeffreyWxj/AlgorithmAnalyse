def lcs_length(str_x, str_y):
    """
    返回最长公共子序列长度
    :return: int length
    """
    m = len(str_x)
    n = len(str_y)
    # 创建动态规划空间
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # 创建公共字符位置标记空间
    flag = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # 初始化对角线的值(上面已初始化每个元素默认值为0)
    # for i in range(1, m + 1):
    #     dp[i][0] = 0
    # for i in range(1, n + 1):
    #     dp[0][i] = 0
    # 开始遍历
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str_x[i - 1] == str_y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                flag[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                flag[i][j] = 2 if dp[i - 1][j] >= dp[i][j - 1] else 3
    get_lcs(len(str_x), len(str_y), str_x, flag)
    return dp[m][n]


def get_lcs(i, j, _str_x, _flags):
    """
    输出动态规划计算出来的最长公共子序列
    :param _flags: 上面算出来的flag
    :return:
    """
    if i == 0 or j == 0:
        return None
    # 从右下角往左上角递归
    if _flags[i][j] == 1:
        # 先递归，然后输出
        get_lcs(i - 1, j - 1, _str_x, _flags)
        print(_str_x[i - 1])
    else:
        # 移位，继续递归
        get_lcs(i - 1, j, _str_x, _flags) if _flags[i][j] == 2 else get_lcs(i, j - 1, _str_x, _flags)


if __name__ == '__main__':
    max_length = lcs_length('cxd6666', 'csxssdssss')
    print('最大长度为：', max_length)
