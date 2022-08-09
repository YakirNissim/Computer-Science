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
    my_tree = Binary_Search_Tree()
    # test 2
    # N = 0
    print('add(50) ', my_tree.add(50))
    print('add(25) ', my_tree.add(25))
    print('add(75) ', my_tree.add(75))
    print('add(70) ', my_tree.add(70))
    print('add(80) ', my_tree.add(80))
    print('add(79) ', my_tree.add(79))
    print('add(78) ', my_tree.add(78))
    print('add(77) ', my_tree.add(77))

    # print('remove(50) ', my_tree.remove(50))
    print('remove(75) ', my_tree.remove(75))

    print('search(78) ', my_tree.search(78)[0])
    # print('search(80) ', my_tree.search(80)[0])
    # print('search(75) ', my_tree.search(75)[0])
    print('search(25) ', my_tree.search(25)[0])


    # # test 1
    # print("add")
    # print('add(5) ', my_tree.add(50))
    # print('add(6) ', my_tree.add(60))
    # print('add(6) ', my_tree.add(60))
    # print('add(7) ', my_tree.add(70))
    # print('add(7) ', my_tree.add(70))
    # print('add(2) ', my_tree.add(20))
    # print('add(1) ', my_tree.add(10))
    # print('add(3) ', my_tree.add(30))
    # print('add(25) ', my_tree.add(25))
    # print('add(58) ', my_tree.add(58))
    # print('add(59) ', my_tree.add(59))
    # # print('search')
    # # print('search(5) ', my_tree.search(5)[0])
    # # print('search(6) ', my_tree.search(6)[0])
    # # print('search(7) ', my_tree.search(7)[0])
    # # print('search(3) ', my_tree.search(3)[0])
    # # print('search(8) ', my_tree.search(8)[0])
    # print('remove')
    # # print('remove(10) ', my_tree.remove(10))
    # print('==========================')
    # print('remove(50) ', my_tree.remove(50))
    # print('==========================')
    # print('search(60) ', my_tree.search(60)[0])
    # print('search(70) ', my_tree.search(70)[0])
    # print('search(10) ', my_tree.search(10)[0])
    # print('search(30) ', my_tree.search(30)[0])
    # print('search(25) ', my_tree.search(25)[0])
    # print('search(59) ', my_tree.search(59)[0])
    #
    # # print('remove(2) ', my_tree.remove(2))
    # # print('remove(1) ', my_tree.remove(1))
    # # print('search(7) ', my_tree.search(7)[0])
    # # print('==========================')
    # # print('remove(5) ', my_tree.remove(5))
    # # print('search(3) ', my_tree.search(3)[0])
    # # print('==========================ppppp')
    # # print('search(7) ', my_tree.search(7)[0])
    # # print('remove(6) ', my_tree.remove(6))
    # # print('search(3) ', my_tree.search(3)[0])
    # # print('==========================')
    # # print('remove(6) ', my_tree.remove(2))



if __name__ == '__main__':
    main()

