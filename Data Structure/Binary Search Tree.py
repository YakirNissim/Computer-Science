class Node (object):
    def __init__(self, data, father=None, left_child=None, right_child=None):
        self.data = data
        self.father = father
        self.left_child = left_child
        self.right_child = right_child

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left_child

    def get_father(self):
        return self.father

    def get_right_child(self):
        return self.right_child

    def set_data(self, new_data):
        self.data = new_data

    def set_father(self, new_father):
        self.father = new_father

    def set_left_child(self, new_left_child):
        self.left_child = new_left_child

    def set_right_child(self, new_right_child):
        self.right_child = new_right_child


class Binary_Search_Tree (object):
    def __init__(self, root=None):
        self.root = root

    def add(self, data, check_node=None):
        if self.root is None:
            self.root = Node(data)
            return True
        elif check_node is None:
            check_node = self.root

        if data < check_node.get_data():
            if check_node.left_child:
                return self.add(data, check_node.get_left_child())
            else:
                new_node = Node(data)
                new_node.set_father([check_node, 'left'])
                check_node.set_left_child(new_node)
                return True
        elif data > check_node.get_data():
            if check_node.right_child:
                return self.add(data, check_node.get_right_child())
            else:
                new_node = Node(data)
                new_node.set_father([check_node, 'right'])
                check_node.set_right_child(new_node)
                return True

        return False

    def search(self, data, check_node=None):
        if self.root is None:
            return False, None
        elif check_node is None:
            check_node = self.root

        print(check_node.get_data())
        if data == check_node.get_data():
            return True, check_node
        elif data < check_node.get_data():
            if check_node.left_child:
                return self.search(data, check_node.get_left_child())
            else:
                return False, None
        elif data > check_node.get_data():
            if check_node.right_child:
                return self.search(data, check_node.get_right_child())
            else:
                return False, None

    def remove(self, data, node=None):
        if node is None:
            x, node = self.search(data)
            if not x:
                return False
        n = 0
        if node.get_left_child():
            n += 1
        if node.get_right_child():
            n += 1
        father = node.get_father()
        print('n= ', n)
        if n == 0:
            if father is None:
                self.root = None
                return True
            elif father[1] == 'left':
                father[0].set_left_child(None)
                return True
            else:
                father[0].set_right_child(None)
                return True
        elif n == 1:
            if node.get_left_child():
                print('left')
                node_child = node.get_left_child()
            else:
                print('right')
                node_child = node.get_right_child()
            if father is None:
                self.root = node_child
                return True
            elif father[1] == 'left':
                father[0].set_left_child(node_child)
                return True
            else:
                father[0].set_right_child(node_child)
                return True
        elif n == 2:
            following_number = node.get_right_child()
            while following_number.get_left_child():
                following_number = following_number.get_left_child()
            node.set_data(following_number.get_data())
            return self.remove(following_number.get_data(), following_number)
        return None


def main():
    pass
    return 0


if __name__ == '__main__':
    main()

