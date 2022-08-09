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
        dataind = len(self.heap) - 1
        while(self.heap[dataind] > self.heap[int(dataind/2)] and dataind > 1):
            # print(f'i = {dataind}')
            # print(f'{self.heap[dataind]} > {self.heap[int(dataind/2)]}')
            self.heap[dataind], self.heap[int(dataind / 2)] = self.heap[int(dataind/2)], self.heap[dataind]
            dataind = int(dataind/2)

    def remove(self, dataind):
        if (len(self.heap) > 1) and (len(self.heap) > dataind > 0):
            self.heap[dataind], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[dataind]
            self.heap = self.heap[:-1]
            self.heapify(dataind, len(self.heap) - 1)
            return True
        return False

    def build_heap(self):
        for i in range(int((len(self.heap) - 1) / 2), 0, -1):
            self.heapify(i, len(self.heap) - 1)

    def heapify(self, i, j):
        maxind = i
        if 2*i <= j and self.heap[2*i] > self.heap[maxind]:
            maxind = 2*i
        if (2*i + 1) <= j and self.heap[2*i + 1] > self.heap[maxind]:
            maxind = 2*i + 1
        if maxind != i:
            self.heap[i], self.heap[maxind] =  self.heap[maxind], self.heap[i]
            self.heapify(maxind, j)

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
        dataind = len(self.heap) - 1
        while(self.heap[dataind] < self.heap[int(dataind/2)] and dataind > 1):
            # print(f'i = {dataind}')
            # print(f'{self.heap[dataind]} > {self.heap[int(dataind/2)]}')
            self.heap[dataind], self.heap[int(dataind / 2)] = self.heap[int(dataind/2)], self.heap[dataind]
            dataind = int(dataind/2)

    def remove(self, dataind):
        if (len(self.heap) > 1) and (len(self.heap) > dataind > 0):
            self.heap[dataind], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[dataind]
            self.heap = self.heap[:-1]
            self.heapify(dataind, len(self.heap) - 1)
            return True
        return False

    def build_heap(self):
        for i in range(int((len(self.heap) - 1) / 2), 0, -1):
            self.heapify(i, len(self.heap) - 1)

    def heapify(self, i, j):
        minind = i
        if 2*i <= j and self.heap[2*i] < self.heap[minind]:
            minind = 2 * i
        if (2*i + 1) <= j and self.heap[2*i + 1] < self.heap[minind]:
            minind = 2 * i + 1
        if minind != i:
            self.heap[i], self.heap[minind] = self.heap[minind], self.heap[i]
            self.heapify(minind, j)

    def get_heap_sort(self):
        old_heap = self.heap
        arr_sort = []
        for i in range(len(self.heap)-1):
            arr_sort += [self.get_root()]
        old_heap[1], old_heap[-1] = old_heap[-1], old_heap[1]  # <== Bug fix
        self.heap = old_heap
        return arr_sort


def main():
    arr = [25, 14, 19, 4, 22, 12, 31, 54, 28, 11]
    print("Max Heap")
    print('sort:')
    print(arr)
    my_heap = MaxHeap(arr)
    print(my_heap.heap)
    print("===========================")
    print('\nget root:')
    print(my_heap.get_root())
    print(my_heap.heap)
    print('=============================')
    print('\nadd data:')
    my_heap.add(60)
    print(my_heap.heap)
    print('=============================')
    print('\nremove:')
    print(my_heap.remove(22))
    print(my_heap.remove(3))
    print(my_heap.heap)
    print(my_heap.remove(2))
    print(my_heap.heap)
    print('=======================')
    print('\nsort:')
    print(my_heap.get_heap_sort())
    print(my_heap.heap)
    print('//////////////////////////////////////////////////////////')
    print("\nMin Heap")
    print('sort:')
    print(arr)
    my_heap = MinHeap(arr)
    print(my_heap.heap)
    print("===========================")
    print('\nget root:')
    print(my_heap.get_root())
    print(my_heap.heap)
    print('=============================')
    print('\nadd data:')
    my_heap.add(6)
    print(my_heap.heap)
    print('=============================')
    print('\nremove:')
    print(my_heap.remove(22))
    print(my_heap.remove(3))
    print(my_heap.heap)
    print(my_heap.remove(2))
    print(my_heap.heap)
    print(my_heap.heap)
    print(my_heap.get_heap_sort())
    print(my_heap.heap)


if __name__ == '__main__':
    main()