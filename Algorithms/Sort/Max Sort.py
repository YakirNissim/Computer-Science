class MaxSort(object):
    def __init__(self, array=[]):
        self.array = array

    def set_array(self, new_array=[]):
        self.array = new_array

    def get_array(self):
        return self.array

    def array_sort(self):
        max_index = 0
        for length in range(len(self.array), 1, -1):
            max_index = self.find_max(length)
            self.array[length - 1], self.array[max_index] = self.array[max_index], self.array[length - 1]

    def find_max(self, length):
        max_index = 0
        for i in range(1, length):
            if self.array[i] > self.array[max_index]:
                max_index = i
        return max_index


def main():  # test
    import random
    my_max_sort = MaxSort()
    n = int(input("n = "))
    my_max_sort.set_array([random.randint(0, 100) for i in range(n)])
    print('The array before sorting:\n', my_max_sort.get_array())
    my_max_sort.array_sort()
    print('The array after sorting:\n', my_max_sort.get_array())
    return 0


if __name__ == '__main__':
    main()
