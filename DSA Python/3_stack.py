class stack(object):
    def __init__(self,size):
        self.arr=[]
        self.size=size

    def push(self,data):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.arr.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            self.arr.pop()

    def show(self):
        temp=self.arr
        temp=temp[::-1]
        for i in temp:
            print(i)
        print()
    
    # returns the last element of stack
    def peek(self):
        print(self.arr[-1])
    def isFull(self):
        if len(self.arr)>=self.size:
            return True
        else:
            return False
    def isEmpty(self):
        if len(self.arr)<=0:
            return True
        else:
            return False
def main():
    s1=stack(2)
    s1.pop()
    s1.push(10)
    s1.push(11)
    s1.push(12)
    s1.show()

#  stack using deque class of collections library
def test_collections():
    import collections
    _stack=collections.deque()
    _stack.append(10)
    _stack.append(12)
    _stack.append(14)
#  stack using deque class 
import queue
def test_queue():
        
    # specify max size of stack
    __stack=queue.LifoQueue(maxsize=10)
    # put method to add element to the stack
    __stack.put(10)
    __stack.put(20)
    print((__stack.queue))
test_queue()


    