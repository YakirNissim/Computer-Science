class DynamicStack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack += [data]
        return True

    def pop(self):
        if len(self.stack) == 0:
            print("The stack is empty!")
            return None
        else:
            data = self.stack[-1]
            self.stack.pop(-1)
            return data


def main():  # test
    my_stack = DynamicStack()
    print("out = ", my_stack.pop())
    print("in 6 = ", my_stack.push(6))
    print("out = ", my_stack.pop())
    print("out = ", my_stack.pop())
    for i in range(11):
        print(f"in {i} = {my_stack.push(i)}")
    print("The stack is:", my_stack.stack)
    for i in range(12):
        print("out = ", my_stack.pop())
    print("The stack is:", my_stack.stack)
    for i in range(15):
        print(f"in {i + 1} = {my_stack.push(i + 1)}")
    print("The stack is:", my_stack.stack)
    return 0


if __name__ == '__main__':
    main()
