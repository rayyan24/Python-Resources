class Node():
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

    def insert(self, data):
        # when data to be inserted is less than the current Node
        if data < self.data:
            if self.leftChild == None:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
# when data to be inserted is greater than the current Node
        else:
            if self.rightChild == None:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)
    def remove(self,node,key):
        if node==None:
            return None
        if key<self.leftChild.data:
            self.leftChild.remove(self.leftChild,key)
        elif key>self.rightChild.data:
            self.leftChild.remove(self.rightChild,key)
        else:
            print("Found")

    def getMinValue(self):
        if self.leftChild == None:
            return self.data
        else:
            return self.leftChild.getMinValue()

    def getMaxValue(self):
        if self.rightChild == None:
            return self.data
        else:
            return self.rightChild.getMaxValue()

    def traverseInOrder(self):
        if self.leftChild != None:
            self.leftChild.traverseInOrder()
        print(self.data)
        if self.rightChild != None:
            self.rightChild.traverseInOrder()


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def traverseInorder(self):
        if self.root != None:
            self.root.traverseInOrder()

    def getMin(self):
        if self.root != None:
            return self.root.getMinValue()

    def getMax(self):
        if self.root != None:
            return self.root.getMaxValue()
    def remove(self,data):
        if self.root!=None:
            self.root.remove(self.root,data)

def main():
    bst1 = BST()
    bst1.insert(110)
    bst1.insert(10)
    bst1.insert(0)
    bst1.insert(180)
    bst1.insert(-180)
    print('Min=', bst1.getMin())
    print("Max=", bst1.getMax())

    bst1.traverseInorder()
    bst1.remove(1110)


main()
