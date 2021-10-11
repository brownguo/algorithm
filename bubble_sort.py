
class bubbleSort(object):
    def __init__(self):
        pass

    def bubble_sort(self, arr):
        for i in range(1, len(arr)):
            for j in range(0, len(arr) - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


if __name__ == '__main__':
    start = bubbleSort()
    resp = start.bubble_sort([3, 6, 9, 2, 4, 1])
    print(resp)
