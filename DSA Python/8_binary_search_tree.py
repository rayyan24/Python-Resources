class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == None:
            self.data = data
            return
        else:
            if data < self.data:
                if self.leftChild == None:
                    self.leftChild = Node(data)
                else:
                    self.leftChild.insert(data)
            else:
                if self.rightChild == None:
                    self.rightChild = Node(data)
                else:
                    self.rightChild.insert(data)

    def search(self, target):
        if self.data == target:
            return True
        else:
            if target < self.data:
                if self.leftChild != None:
                    if self.leftChild.search(target) == True:
                        return True
                    else:
                        return False
            else:
                if self.rightChild != None:
                    if self.rightChild.search(target) == True:
                        return True
                    else:
                        return False
    def traversePreorder(self):
        if self.data==None:
            print("Tree is Empty")
        else:
            print(self.data,end=" ")
            if self.leftChild!=None:
                self.leftChild.traversePreorder()
            if self.rightChild!=None:
                self.rightChild.traversePreorder()
                
    def traverseInorder(self):
        if self.data==None:
            print("Tree is Empty")
        else:
            if self.leftChild!=None:
                self.leftChild.traverseInorder()
            print(self.data,end=" ")
            if self.rightChild!=None:
                self.rightChild.traverseInorder()
                
    def traversePostrder(self):
        if self.data==None:
            print("Tree is Empty")
        else:
            if self.leftChild!=None:
                self.leftChild.traversePostrder()
            if self.rightChild!=None:
                self.rightChild.traversePostrder()
            print(self.data,end=" ")
    def getMin(self):
        if self.leftChild==None:
            return self.data
        else:
            return self.leftChild.getMin()
    def getMax(self):
        if self.rightChild==None:
            return self.data
        else:
            return self.rightChild.getMax()

class BST:
    def __init__(self) -> None:
        self.root = Node(None)

    def insert(self, data):
        self.root.insert(data)
        print(f"{data} inserted")

    def search(self, toFind):
        if self.root.search(toFind) == True:
            print(f"{toFind} is Found")
        else:
            print(f"{toFind} is not Found")
    def traverse(self,preorder=None,inorder=None,postorder=None):
        if preorder==True:
            self.root.traversePreorder()
            print()
        if inorder==True:
            self.root.traverseInorder()
            print()
        if postorder==True:
            self.root.traversePostrder()
            print()
    def getMin(self):
        if self.root.data==None:
            print("Tree is Empty")
        else:
            min=self.root.getMin()
            print(min)
    def getMax(self):
        if self.root.data==None:
            print("Tree is Empty")
        else:
            max=self.root.getMax()
            print(max)

def main():
    bst1 = BST()
    bst1.insert(10)
    bst1.insert(12)
    bst1.insert(9)
    bst1.insert(7)
    bst1.insert(17)
    bst1.insert(27)
    bst1.search(12)
    bst1.search(122)
    bst1.getMax()
    bst1.traverse(inorder=1)
main()
