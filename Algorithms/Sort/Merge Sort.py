class MergeSort(object):
    array = None

    @classmethod
    def sort(cls, array):
        return cls.array_sort_recursive_function(array)

    @classmethod
    def array_sort_recursive_function(cls, array):
        a, b = cls.array_cutting(array)
        if len(a) > 1:
            a = cls.array_sort_recursive_function(a)
        if len(b) > 1:
            b = cls.array_sort_recursive_function(b)
        return cls.merging_sorted_arrays(a, b)

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
    n = int(input("n = "))
    my_array = [random.randint(0, 100) for i in range(n)]
    print('The array before sorting:\n', my_array)
    my_array = MergeSort.sort(my_array)
    print('The array after sorting:\n', my_array)
    return 0


if __name__ == '__main__':
    main()
