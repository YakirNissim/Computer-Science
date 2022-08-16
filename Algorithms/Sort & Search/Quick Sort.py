class BubbleSort(object):
    array = None

    @classmethod
    def sort(cls, array):
        cls.array = array
        cls.array_sort_recursive_function(0, len(array)-1)
        return cls.array

    @classmethod
    def array_sort_recursive_function(cls, start_index, end_index):
        cls.array[int((end_index - start_index)/2 + start_index)],\
            cls.array[start_index] = cls.array[start_index], cls.array[int((end_index - start_index)/2 + start_index)]
        bottom = start_index+1
        top = end_index
        pivot = cls.array[start_index]
        while top >= bottom:
            while top >= bottom and pivot > cls.array[bottom]:
                bottom += 1
            while top >= bottom and pivot <= cls.array[top]:
                top -= 1
            if top >= bottom and cls.array[bottom] >= pivot > cls.array[top]:
                cls.array[top], cls.array[bottom] = cls.array[bottom], cls.array[top]
        cls.array[top], cls.array[start_index] = cls.array[start_index], cls.array[top]
        if top - start_index > 1:
            cls.array_sort_recursive_function(start_index, top-1)
        if end_index - top > 1:
            cls.array_sort_recursive_function(top+1, end_index)


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
