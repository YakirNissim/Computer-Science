class BinarySearch(object):
    @staticmethod
    def search(array, x):
        low_index = 0
        high_index = len(array) - 1
        while high_index >= low_index:
            mid = int((high_index + low_index)/2)
            if x < array[mid]:
                high_index = mid-1
            elif x > array[mid]:
                low_index = mid+1
            else:
                return mid
        return None
        pass


def main():  # test
    my_array = [2, 24, 24, 27, 28, 46, 47, 55, 67, 86, 92, 99]
    num = int(input("num = "))
    result = BinarySearch.search(my_array, num)
    if result is None:
        print("The number was not found!")
    else:
        print(f"The number is found and its index is {result}")
    return 0


if __name__ == '__main__':
    main()
