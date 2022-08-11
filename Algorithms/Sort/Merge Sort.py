class MergeSort(object):
    def __init__(self, array=[]):
        self.array = array

    def set_array(self, new_array=[]):
        self.array = new_array

    def get_array(self):
        return self.array

    def array_sort(self):
        self.array = self.array_sort_recursive_function(self.array)

    def array_sort_recursive_function(self, array):
        a, b = self.array_cutting(array)
        if len(a) > 1:
            a = self.array_sort_recursive_function(a)
        if len(b) > 1:
            b = self.array_sort_recursive_function(b)
        return self.merging_sorted_arrays(a, b)

    @staticmethod
    def array_cutting(array):
        return array[:int(len(array) / 2)], array[int(len(array) / 2):]

    @staticmethod
    def merging_sorted_arrays(a, b):
        arr_sort = []
        ia = 0
        ib = 0
        for i in range(len(a) + len(b)):
            if ia < len(a) and ib < len(b):
                if a[ia] < b[ib]:
                    arr_sort += [a[ia]]
                    ia += 1
                else:
                    arr_sort += [b[ib]]
                    ib += 1
            elif ia < len(a):
                arr_sort += a[ia:]
                return arr_sort
            elif ib < len(b):
                arr_sort += b[ib:]
                return arr_sort
        return arr_sort


def main():  # test
    import random
    my_merge_sort = MergeSort()
    n = int(input("n = "))
    my_merge_sort.set_array([random.randint(0, 100) for i in range(n)])
    print('The array before sorting:\n', my_merge_sort.get_array())
    my_merge_sort.array_sort()
    print('The array after sorting:\n', my_merge_sort.get_array())
    return 0


if __name__ == '__main__':
    main()
