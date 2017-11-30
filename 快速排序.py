def q_sort(arr, p, r):
    if p < r:
        # 执行快速排序，获取分割点
        q = q_partition(arr, p, r)
        # 左侧递归排序
        q_sort(arr, p, q - 1)
        # 右侧递归排序
        q_sort(arr, q + 1, r)


def q_partition(arr, p, r):
    # 储存左右端点
    i = p
    j = r
    # 储存左侧第一个元素作为比较中心点
    x = arr[p]
    # 循环
    while True:
        # 从左侧开始找大于x的元素，不断向右移动指针
        while arr[i] <= x and i < r:
            i += 1
        # 从右侧开始找小于x的元素，不断向左移动指针
        while arr[j] > x:
            j -= 1
        # 越界则退出排序
        if i >= j:
            break
        # 交换
        swap(arr, i, j)
    # 把x放到中心点
    arr[p] = arr[j]
    arr[j] = x
    # 返回中心点坐标
    return j


def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    print(arr)


if __name__ == '__main__':
    _ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    q_sort(_ls, 0, 8)
    print(_ls)
