class BucketSort(object):
    array = None
    max_num_in_range = None
    histogram_array = None

    @classmethod
    def sort(cls, array, max_num_in_range):
        cls.array = array
        cls.max_num_in_range = max_num_in_range
        cls.array_histogram()
        cls.array = [num for num in range(max_num_in_range+1) for i in range(cls.histogram_array[num])]
        return cls.array

    @classmethod
    def array_histogram(cls):
        cls.histogram_array = [0 for i in range(cls.max_num_in_range+1)]
        for num in cls.array:
            cls.histogram_array[num] += 1


def main():  # test
    import random
    n = int(input("n = "))
    my_array = [random.randint(0, 100) for i in range(n)]
    print('The array before sorting:\n', my_array)
    my_array = BucketSort.sort(my_array, 100)
    print('The array after sorting:\n', my_array)
    return 0


if __name__ == '__main__':
    main()
