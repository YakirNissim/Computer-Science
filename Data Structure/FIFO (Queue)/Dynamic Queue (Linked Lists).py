class DynamicQueue(object):
    def __init__(self):
        self.back = None
        self.front = None
        self.size = 0

    def enqueue(self, data):
        if self.back is None:
            self.back = self.front = Node(data)
        else:
            temp_node = Node(data)
            self.back.set_next_node(temp_node)
            self.back = temp_node
        self.size += 1
        return True

    def dequeue(self):
        if self.front is None:
            print("The queue is empty!")
            return None
        data = self.front.get_data()
        self.front = self.front.get_next_node()
        self.size -= 1
        if self.front is None:
            self.back = None
        return data

    def get_size(self):
        return self.size

    def get_list_of_linked_list(self):
        this_node = self.front
        return_list = []
        while this_node:
            return_list += [this_node.get_data()]
            this_node = this_node.get_next_node()
        return return_list


class Node (object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


def main():  # test
    my_queue = DynamicQueue()
    print("out = ", my_queue.dequeue())
    print("in = ", my_queue.enqueue(6))
    print("out = ", my_queue.dequeue())
    print("out = ", my_queue.dequeue())
    for i in range(11):
        print("in = ", my_queue.enqueue(i))
    print(f"list of Linked-List is: {my_queue.get_list_of_linked_list()} "
          f"and the size it {my_queue.get_size()}")
    for i in range(12):
        print("out = ", my_queue.dequeue())
    print(f"list of Linked-List is: {my_queue.get_list_of_linked_list()} "
          f"and the size it {my_queue.get_size()}")
    print(f"front = {my_queue.front}, back = {my_queue.back}")
    for i in range(15):
        print("in = ", my_queue.enqueue(i+1))
    print(f"list of Linked-List is: {my_queue.get_list_of_linked_list()} "
          f"and the size it {my_queue.get_size()}")
    return 0


if __name__ == '__main__':
    main()
