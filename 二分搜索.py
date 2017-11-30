def binary_search(_list, _target):
    left = 0
    right = len(_list) - 1
    while left <= right:
        middle = int((left + right) >> 1)
        if _list[middle] == _target:
            i = j = middle
            return middle, i, j
        if _list[middle] > _target:
            right = middle - 1
        else:
            left = middle + 1
    i = right
    j = left
    return -1, i, j


if __name__ == '__main__':
    _ls = [1, 2, 3, 4, 6, 7, 8, 9]
    print(binary_search(_ls, 6))
    print(binary_search(_ls, 2.5))
