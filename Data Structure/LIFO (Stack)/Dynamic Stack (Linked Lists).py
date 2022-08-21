class DynamicStack(object):
    def __init__(self):
        self.first_element_stack = None
        self.size = 0

    def push(self, data):
        self.first_element_stack = Node(data, self.first_element_stack)
        self.size += 1
        return True

    def pop(self):
        if self.first_element_stack is None:
            print("The stack is empty!")
            return None
        else:
            data = self.first_element_stack.get_data()
            self.first_element_stack = self.first_element_stack.get_next_node()
            self.size -= 1
            return data

    def get_size(self):
        return self.size

    def get_list_of_linked_list(self):
        this_node = self.first_element_stack
        return_list = []
        while this_node:
            return_list += [this_node.get_data()]
            this_node = this_node.get_next_node()
        return return_list


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


def main():  # test
    my_stack = DynamicStack()
    print("out = ", my_stack.pop())
    print("in 6 = ", my_stack.push(6))
    print("out = ", my_stack.pop())
    print("out = ", my_stack.pop())
    for i in range(11):
        print(f"in {i} = {my_stack.push(i)}")
    print(f"list of Linked-List is: {my_stack.get_list_of_linked_list()} "
          f"and the size it {my_stack.get_size()}")
    for i in range(12):
        print("out = ", my_stack.pop())
    print(f"list of Linked-List is: {my_stack.get_list_of_linked_list()} "
          f"and the size it {my_stack.get_size()}")
    for i in range(15):
        print(f"in {i + 1} = {my_stack.push(i + 1)}")
    print(f"list of Linked-List is: {my_stack.get_list_of_linked_list()} "
          f"and the size it {my_stack.get_size()}")
    return 0


if __name__ == '__main__':
    main()