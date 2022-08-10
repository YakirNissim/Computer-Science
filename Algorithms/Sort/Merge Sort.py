class MergeSort(object):
    def __init__(self, array=[]):
        self.array = array

    def Set_array(self, new_array=[]):
        self.array = new_array

    def Get_array(self):
        return self.array

    def Array_sort(self):
        self.array = self.Array_sort_recursive_function(self.array)

    def Array_sort_recursive_function(self, array):
        a, b = self.Array_cutting(array)
        if len(a) > 1:
            a = self.Array_sort_recursive_function(a)
        if len(b) > 1:
            b = self.Array_sort_recursive_function(b)
        return self.Merging_sorted_arrays(a, b)

    @staticmethod
    def Array_cutting(array):
        return array[:int(len(array) / 2)], array[int(len(array) / 2):]

    @staticmethod
    def Merging_sorted_arrays(a, b):
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
    my_merge_sort.Set_array([random.randint(0, 100) for i in range(n)])
    print('The array before sorting:\n', my_merge_sort.Get_array())
    my_merge_sort.Array_sort()
    print('The array after sorting:\n', my_merge_sort.Get_array())


if __name__ == '__main__':
    main()
