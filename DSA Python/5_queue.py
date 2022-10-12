class Queue:
    def __init__(self, size):
        self.arr = []
        self.size = size

    def isEmpty(self):
        if not self.arr:
            return True
        else:
            return False

    def isFull(self):
        if len(self.arr) >= self.size:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow")
        else:
            self.arr.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            self.arr.pop(0)

    def showQueue(self):
        for i in self.arr:
            print(i, end=" ")
        print()

    def __str__(self) -> str:
        if self.isEmpty():
            return "Queue Underflow"
        return " ".join([str(i) for i in self.arr])


def main():
    queue1 = Queue(size=10)
    queue1.enqueue(10)
    queue1.enqueue(12)
    queue1.enqueue(13)
    print(queue1)
    queue1.dequeue()
    print(queue1)
    # a=[1,2,3]
    # a.append(11,12)
    # print(a)

main()
