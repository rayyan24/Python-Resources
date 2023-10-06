'''
DFS Algorithm
1 Initialize the stack with the starting Node
2 Pop the node on top of stack 
3 Perform any operation on the node
4 Append all the nodes in the neighbour of popped node into the stack
5 perform steps 2 to 4 until the stack is empty
6 Maintain a visited set to ensure that a single node is not visited again
'''
def main():
    graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }
    # traversal=dfsIterative(graph,"5")
    # traversal=dfsRecursive(graph,"5")
    traversal=bfs(graph,"5")
    print(traversal)

def dfsIterative(adjList,start):
    # set does not maintain its order 
    traversal=list()
    visited=set()
    stack=[start]
    while len(stack)>0:
        curentNode=stack.pop()
        traversal.append(curentNode)
        visited.add(curentNode)
        for neighbour in adjList[curentNode]:
            if neighbour not in visited:
                stack.append(neighbour)
    return list(traversal)

def dfsRecursive(adjList,start,res=list(),visited=set()):
    if start in visited:
        return
    res.append(start)
    visited.add(start)
    for i in adjList[start]:
        dfsRecursive(adjList,i,res,visited)
    return res
'''
BFS Algorithm
1 Initialize Queue with the starting node
2 Pop the first element in the Queue
3 Perform any operation needed on the node
4 Append all the neighbours of popped node to the queue
5 Repeat step until queue goes empty 
'''
def bfs(adjList,start):
    queue=[start]
    visited=set(start)
    res=[]
    while len(queue)>0:
        currentElem=queue.pop(0)
        res.append(currentElem)
        for i in adjList[currentElem]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return res
if __name__=="__main__":
    main()