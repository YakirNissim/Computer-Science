class CircularQueue(object):
    def __init__(self, length_queue):
        self.back_index = self.front_index = 0
        self.full_queue = False
        self.length_queue = length_queue
        self.queue = [None for i in range(length_queue)]
        pass

    def enqueue(self, data):
        if self.full_queue:
            print("The queue is full!")
            return False
        else:
            self.queue[self.back_index] = data
            self.back_index = (self.back_index + 1) % self.length_queue
            if self.back_index == self.front_index:
                self.full_queue = True
            return True

    def dequeue(self):
        if self.front_index == self.back_index and not self.full_queue:
            print("The queue is empty!")
            return None
        else:
            data = self.queue[self.front_index]
            if self.full_queue:
                self.full_queue = False
            self.front_index = (self.front_index+1) % self.length_queue
            return data


def main():  # test
    my_queue = CircularQueue(10)
    print("out = ", my_queue.dequeue())
    print("in = ", my_queue.enqueue(6))
    print("out = ", my_queue.dequeue())
    print("out = ", my_queue.dequeue())
    for i in range(11):
        print("in = ", my_queue.enqueue(i))
    print("The whole list is:", my_queue.queue)
    print(f"front_index = {my_queue.front_index}, back_index = {my_queue.back_index}")
    for i in range(12):
        print("out = ", my_queue.dequeue())
    print("The whole list is:", my_queue.queue)
    print(f"front_index = {my_queue.front_index}, back_index = {my_queue.back_index}")
    for i in range(11):
        print("in = ", my_queue.enqueue(i+1))
    print("The whole list is:", my_queue.queue)
    print(f"front_index = {my_queue.front_index}, back_index = {my_queue.back_index}")
    return 0


if __name__ == '__main__':
    main()
