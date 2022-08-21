class Node (object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList (object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        self.root = Node(data, self.root)
        self.size += 1

    def add_after(self, data, after):
        find, node = self.find(after)
        if find:
            while node.get_next_node().get_data() == after:
                node = node.get_next_node()
            node.set_next_node(Node(data, node.get_next_node()))
            self.size += 1
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def remove(self, data):
        check_node = self.root
        beck_node = None
        while check_node:
            if data == check_node.get_data():
                if not beck_node:
                    self.root = check_node.get_next_node()
                else:
                    beck_node.set_next_node(check_node.get_next_node())
                self.size -= 1
                return True
            beck_node = check_node
            check_node = beck_node.get_next_node()
        return False

    def find(self, data):
        check_node = self.root
        while check_node:
            if data == check_node.get_data():
                return True, check_node
            check_node = check_node.get_next_node()
        return False, None

    def get_list_of_linked_list(self):
        this_node = self.root
        return_list = []
        while this_node:
            return_list += [this_node.get_data()]
            this_node = this_node.get_next_node()
        return return_list


def main():  # test
    my_LinkedList = LinkedList()
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 7:")
    print(my_LinkedList.find(7))
    for i in range(11):
        print(f"add {i}")
        my_LinkedList.add(i)
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 7:")
    print(my_LinkedList.find(7))
    print("remove 7:")
    print(my_LinkedList.remove(7))
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 7:")
    print(my_LinkedList.find(7))
    print("add 44 after 2:")
    print(my_LinkedList.add_after(44, 2))
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 44:")
    print(my_LinkedList.find(44))
    print("add 7 after 2:")
    print(my_LinkedList.add_after(7, 2))
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 7:")
    print(my_LinkedList.find(7))
    print("add 7 after 2:")
    print(my_LinkedList.add_after(7, 2))
    print("add 7 after 2:")
    print(my_LinkedList.add_after(7, 2))
    print("add 17 after 7:")
    print(my_LinkedList.add_after(17, 7))
    print(f"list of Linked-List is: {my_LinkedList.get_list_of_linked_list()} "
          f"and the size it {my_LinkedList.get_size()}")
    print("find 7:")
    print(my_LinkedList.find(7))
    return 0


if __name__ == "__main__":
    main()
