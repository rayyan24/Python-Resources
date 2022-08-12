from hashlib import new
import tarfile


class Node:
    def __init__(self, data) -> None:
        self.prevNode=None
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def showList(self):
        if self.head == None:
            print("Linled List is Empty")
        else:
            tempNode = self.head
            while(tempNode is not None):
                print(tempNode.data, end=" ")
                tempNode = tempNode.nextNode
            print()
    def insertStart(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            oldHead=self.head
            new_node.nextNode=oldHead
            oldHead.prevNode=new_node
            self.head=new_node

    def insertEnd(self, data):
        temp=self.head
        while temp.nextNode!=None:
            temp=temp.nextNode
        else:
            new_node=Node(data)
            temp.nextNode=new_node
            new_node.prevNode=temp
    def insertAfter(self,data,target):

        temp=self.head
        while temp != None:
            if temp.data==target:
                break
            else:
                temp=temp.nextNode        
        if temp == None:
            print("{} not found".format(target))
        else:
            print(temp.data)
            new_node=Node(data)

            new_node.nextNode=temp.nextNode
            temp.nextNode.prevNode=new_node
            temp.nextNode=new_node
            new_node.prevNode=temp
            
            # currentNode=temp.nextNode
            # new_node.prevNode=currentNode.prevNode
            # temp.nextNode=new_node
            # new_node.nextNode=currentNode
            # currentNode.prevNode=new_node

            
    def insertBefore(self,data,target):
        if self.head.data==target:
            self.insertStart(data)
            return 
        else:
            temp=self.head
            while temp.nextNode!=None:
                if temp.nextNode.data==target:
                    break
                else:
                    temp=temp.nextNode
        if temp.nextNode == None:
            print("{} not found".format(target))
        else:
            new_node=Node(data)
            currentNext=temp.nextNode
            new_node.prevNode=temp
            new_node.nextNode=temp.nextNode
            temp.nextNode=new_node
    def remove(self,start=None,end=None,target=None):
        try:
            # remove the first node
            if start==True:
                if self.head==None:
                    print("Linked List is Empty")
                else:
                    self.head=self.head.nextNode
                    self.head.prevNode=None
            # remove the last node
            if end==True:
                if self.head==None:
                    print("Linked List is Empty")
                else:
                    temp=self.head
                    while temp!=None:
                        if temp.nextNode.nextNode==None:
                            break
                        else:
                            temp=temp.nextNode
                    temp.nextNode=None
            
            # remove the node containing target value
            if target!=None:
                if self.head==None:
                    print("Linked List is Empty")
                elif target==self.head.data:
                    self.remove(start=True)
                else:
                    temp=self.head
                    while temp.nextNode!=None:
                        if temp.nextNode.data==target:
                            break
                        else:
                            temp=temp.nextNode
                    if temp.nextNode==None:
                        print("Cannot remove {} Element Not Found".format(target))
                    else:
                        temp.nextNode=temp.nextNode.nextNode
        except Exception as e:
            print("Linked List is Empty")
            self.head=None
    def traverseReverse(self):
        n=self.head
        while n.nextNode is not None:
            n=n.nextNode
        while n.prevNode is not None:
            print(n.data,end=" ")
            n=n.prevNode
        print(n.data)


def main():
    l1=LinkedList()
    l1.insertStart(12)
    l1.insertStart(11)
    l1.insertStart(114)
    l1.insertStart(112)
    l1.insertEnd(77777)
    l1.showList()
    l1.insertAfter(213,11)
    l1.showList()
    l1.insertBefore(0,1131)
    l1.showList()
    l1.remove(end=True)
    l1.showList()
    l1.traverseReverse()
main()