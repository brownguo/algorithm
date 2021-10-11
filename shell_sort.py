import math


class shellSort(object):
    def __init__(self):
        pass

    def shell_sort(self, arr):
        gap = 1
        while(gap < len(arr) / 3):
            gap = gap * 3 + 1
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i-gap
                while j >= 0 and arr[j] > temp:
                    arr[j+gap] = arr[j]
                arr[j+gap] = temp
            gap = math.floor(gap / 3)

        print(arr)


if __name__ == '__main__':
    start = shellSort()
    start.shell_sort([3, 6, 9, 2, 4, 1])
