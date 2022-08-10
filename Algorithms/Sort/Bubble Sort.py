class BubbleSort(object):
    def __init__(self, array=[]):
        self.array = array

    def Set_array(self, new_array=[]):
        self.array = new_array

    def Get_array(self):
        return self.array

    def Array_sort(self):
        not_sorted = True
        sort_index = len(self.array)
        while len(self.array) > 1 and not_sorted:
            not_sorted = self.bubble(sort_index)
            sort_index -= 1

    def bubble(self, sort_index):
        swapped = False
        for i in range(1, sort_index):
            if self.array[i-1] > self.array[i]:
                self.array[i - 1], self.array[i] = self.array[i], self.array[i-1]
                swapped = True
        return swapped


def main():  # test
    import random
    my_merge_sort = BubbleSort()
    n = int(input("n = "))
    my_merge_sort.Set_array([random.randint(0, 100) for i in range(n)])
    print('The array before sorting:\n', my_merge_sort.Get_array())
    my_merge_sort.Array_sort()
    print('The array after sorting:\n', my_merge_sort.Get_array())


if __name__ == '__main__':
    main()

