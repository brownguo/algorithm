
class selectSort(object):
    def __init__(self):
        pass

    def select_sort(self, arr):
        for i in range(len(arr) - 1):
            minIdx = i  # 最小索引
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIdx]:
                    minIdx = j
            if i != minIdx:     # i 不是最小数时，将 i 和最小数进行交换
                arr[i], arr[minIdx] = arr[minIdx], arr[i]
        print(arr)


if __name__ == '__main__':
    start = selectSort()
    start.select_sort([3, 6, 9, 2, 4, 1])
