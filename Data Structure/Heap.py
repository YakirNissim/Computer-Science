class MaxHeap(object):
    def __init__(self, arr=[]):
        self.heap = [0] + arr
        if len(arr):
            self.build_heap()

    def get_root(self):
        if len(self.heap) > 1:
            root = self.heap[1]
            self.remove(1)
            return root

    def add(self, data):
        self.heap += [data]
        data_index = len(self.heap) - 1
        while self.heap[data_index] > self.heap[int(data_index / 2)] and data_index > 1:
            self.heap[data_index], self.heap[int(data_index / 2)] = self.heap[int(data_index / 2)], self.heap[data_index]
            data_index = int(data_index / 2)

    def remove(self, data_index):
        if (len(self.heap) > 1) and (len(self.heap) > data_index > 0):
            self.heap[data_index], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[data_index]
            self.heap = self.heap[:-1]
            self.heapify(data_index, len(self.heap) - 1)
            return True
        return False

    def build_heap(self):
        for i in range(int((len(self.heap) - 1) / 2), 0, -1):
            self.heapify(i, len(self.heap) - 1)

    def heapify(self, i, j):
        max_index = i
        if 2*i <= j and self.heap[2*i] > self.heap[max_index]:
            max_index = 2 * i
        if (2*i + 1) <= j and self.heap[2*i + 1] > self.heap[max_index]:
            max_index = 2 * i + 1
        if max_index != i:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.heapify(max_index, j)

    def get_heap_sort(self):
        old_heap = self.heap
        arr_sort = []
        for i in range(len(self.heap)-1):
            arr_sort = [self.get_root()] + arr_sort
        old_heap[1], old_heap[-1] = old_heap[-1], old_heap[1]  # <== Bug fix
        self.heap = old_heap
        return arr_sort


class MinHeap(object):
    def __init__(self, arr=[]):
        self.heap = [0] + arr
        if len(arr):
            self.build_heap()

    def get_root(self):
        if len(self.heap) > 1:
            root = self.heap[1]
            self.remove(1)
            return root

    def add(self, data):
        self.heap += [data]
        data_index = len(self.heap) - 1
        while self.heap[data_index] < self.heap[int(data_index / 2)] and data_index > 1:
            self.heap[data_index], self.heap[int(data_index / 2)] = self.heap[int(data_index / 2)], self.heap[data_index]
            data_index = int(data_index / 2)

    def remove(self, data_index):
        if (len(self.heap) > 1) and (len(self.heap) > data_index > 0):
            self.heap[data_index], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[data_index]
            self.heap = self.heap[:-1]
            self.heapify(data_index, len(self.heap) - 1)
            return True
        return False

    def build_heap(self):
        for i in range(int((len(self.heap) - 1) / 2), 0, -1):
            self.heapify(i, len(self.heap) - 1)

    def heapify(self, i, j):
        min_index = i
        if 2*i <= j and self.heap[2*i] < self.heap[min_index]:
            min_index = 2 * i
        if (2*i + 1) <= j and self.heap[2*i + 1] < self.heap[min_index]:
            min_index = 2 * i + 1
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.heapify(min_index, j)

    def get_heap_sort(self):
        old_heap = self.heap
        arr_sort = []
        for i in range(len(self.heap)-1):
            arr_sort += [self.get_root()]
        old_heap[1], old_heap[-1] = old_heap[-1], old_heap[1]  # <== Bug fix
        self.heap = old_heap
        return arr_sort


def main():
    pass
    return 0


if __name__ == '__main__':
    main()
