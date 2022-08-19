class BubbleSort(object):
    array = None

    @classmethod
    def sort(cls, array):
        cls.array = array
        not_sorted = True
        sort_index = len(cls.array)
        while len(cls.array) > 1 and not_sorted:
            not_sorted = cls.bubble(sort_index)
            sort_index -= 1

    @classmethod
    def bubble(cls, sort_index):
        swapped = False
        for i in range(1, sort_index):
            if cls.array[i - 1] > cls.array[i]:
                cls.array[i - 1], cls.array[i] = cls.array[i], cls.array[i - 1]
                swapped = True
        return swapped


def main():  # test
    import random
    n = int(input("n = "))
    my_array = [random.randint(0, 100) for i in range(n)]
    print('The array before sorting:\n', my_array)
    BubbleSort.sort(my_array)
    print('The array after sorting:\n', my_array)
    return 0


if __name__ == '__main__':
    main()

