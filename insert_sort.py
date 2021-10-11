
class insertSort(object):
    def __init__(self):
        pass

    def insert_sort(self, arr):
        for i in range(len(arr)):
            preIndex = i-1
            current = arr[i]
            while preIndex >= 0 and arr[preIndex] > current:
                arr[preIndex+1] = arr[preIndex]
                preIndex -= 1
            arr[preIndex+1] = current
        print(arr)


if __name__ == '__main__':
    start = insertSort()
    start.insert_sort([3, 6, 9, 2, 4, 1])
