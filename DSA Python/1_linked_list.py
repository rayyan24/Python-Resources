class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None

    def showList(self):
        if self.head == None:
            print("Linled List is Empty")
        else:
            tempNode = self.head
            while(tempNode is not None):
                print(tempNode.data, end=" ")
                tempNode = tempNode.nextNode
            print()
    def insertStart(self, data):
        tempNode = Node(data)
        if self.head == None:
            self.head = tempNode
        else:
            tempNode.nextNode = self.head
            self.head = tempNode

    def insertEnd(self, data):
        tempNode = self.head
        while(tempNode.nextNode != None):
            tempNode = tempNode.nextNode
        tempNode.nextNode = Node(data)
        # making the list circular  
        # tempNode.nextNode.nextNode=self.head
    def insertAfter(self,data,target):
        # if target==self.head.data:
        #     self.insertStart(data)
        #     self.remove(data)
        temp=self.head
        while temp != None:
            if temp.data==target:
                break
            else:
                temp=temp.nextNode        
        if temp == None:
            print("{} not found".format(target))
        else:
            newNode=Node(data)
            newNode.nextNode=temp.nextNode
            temp.nextNode=newNode

# ********* insert before using insertAfter function
    # def insertBefore(self,data,target):
    #     if target==self.head.data:
    #         self.insertStart(data)
    #     else:
    #         temp=self.head
    #         while temp!=None and temp.nextNode!= None:
    #             if temp.nextNode.data==target:
    #                 self.insertAfter(data,temp.data)
    #                 break
    #             else:
    #                 temp=temp.nextNode
    #         if temp.nextNode==None:
    #                 print("{} not found".format(target))
    def insertBefore(self,data,target):
        if target==self.head.data:
            self.insertStart(data)
        else:
            temp=self.head
            while temp!=None:
                if temp.nextNode.data==target:
                    break
                else:
                    temp=temp.nextNode
            if temp==None:
                    print("{} not found".format(target))
            else:
                new_node=Node(data)
                new_node.nextNode=temp.nextNode
                temp.nextNode=new_node
            
    def remove(self, data):
        if self.head.data==data:
            self.head=self.head.nextNode
        else:
            tempNode = self.head
            while tempNode.nextNode != None:
                if tempNode.nextNode.data == data:
                    temp = tempNode.nextNode
                    tempNode.nextNode = tempNode.nextNode.nextNode
                    del temp
                    return 1
                else:
                    tempNode = tempNode.nextNode
            print("Cannot remove {} Element Not Found".format(data))
    def removeEnd(self):
        temp=self.head
        while temp.nextNode.nextNode!= None:
            temp=temp.nextNode
        temp.nextNode=None
def main():
    l1 = LinkedList()
    l1.insertStart(11)
    l1.insertEnd(12)
    l1.insertEnd(13)
    l1.insertBefore(1345,11)
    l1.remove(13453)
    l1.showList()
    l1.removeEnd()
    l1.showList()
    l1.insertAfter(999,11)
    l1.showList()

main()
