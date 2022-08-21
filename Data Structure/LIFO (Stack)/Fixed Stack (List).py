class FixedStack(object):
    def __init__(self, length_stack):
        self.first_index = -1
        self.length_stack = length_stack
        self.stack = [None for i in range(length_stack)]

    def push(self, data):
        if self.first_index < self.length_stack-1:
            self.first_index += 1
            self.stack[self.first_index] = data
            return True
        else:
            print("The stack is full!")
            return False

    def pop(self):
        if self.first_index < 0:
            print("The stack is empty!")
            return None
        else:
            data = self.stack[self.first_index]
            self.stack[self.first_index] = None
            self.first_index -= 1
            return data


def main():  # test
    my_stack = FixedStack(10)
    print("out = ", my_stack.pop())
    print("in 6 = ", my_stack.push(6))
    print("out = ", my_stack.pop())
    print("out = ", my_stack.pop())
    for i in range(11):
        print(f"in {i} = {my_stack.push(i)}")
    print("The stack is:", my_stack.stack)
    print(f"first_index = {my_stack.first_index}")
    for i in range(12):
        print("out = ", my_stack.pop())
    print("The stack is:", my_stack.stack)
    print(f"first_index = {my_stack.first_index}")
    for i in range(11):
        print(f"in {i+1} = {my_stack.push(i+1)}")
    print("The stack is:", my_stack.stack)
    print(f"first_index = {my_stack.first_index}")
    return 0


if __name__ == '__main__':
    main()
