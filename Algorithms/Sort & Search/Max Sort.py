class MaxSort(object):
    array = None

    @classmethod
    def sort(cls, array):
        cls.array = array
        max_index = 0
        for length in range(len(cls.array), 1, -1):
            max_index = cls.find_max(length)
            cls.array[length - 1], cls.array[max_index] = cls.array[max_index], cls.array[length - 1]

    @classmethod
    def find_max(cls, length):
        max_index = 0
        for i in range(1, length):
            if cls.array[i] > cls.array[max_index]:
                max_index = i
        return max_index


def main():  # test
    import random
    n = int(input("n = "))
    my_array = [random.randint(0, 100) for i in range(n)]
    print('The array before sorting:\n', my_array)
    MaxSort.sort(my_array)
    print('The array after sorting:\n', my_array)
    return 0


if __name__ == '__main__':
    main()