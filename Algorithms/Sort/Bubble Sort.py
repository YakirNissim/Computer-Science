class BubbleSort(object):
    def __init__(self, array=[]):
        self.array = array

    def set_array(self, new_array=[]):
        self.array = new_array

    def get_array(self):
        return self.array

    def array_sort(self):
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
    my_bubble_sort = BubbleSort()
    n = int(input("n = "))
    my_bubble_sort.set_array([random.randint(0, 100) for i in range(n)])
    print('The array before sorting:\n', my_bubble_sort.get_array())
    my_bubble_sort.array_sort()
    print('The array after sorting:\n', my_bubble_sort.get_array())
    return 0


if __name__ == '__main__':
    main()

