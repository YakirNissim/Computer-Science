class Node (object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def ser_data(self, new_data):
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


def main():
    pass
    return 0


if __name__ == "__main__":
    main()
