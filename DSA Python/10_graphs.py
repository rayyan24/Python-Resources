class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.matrix = []
        
    def addNode(self, val) -> None:
        if val in self.nodes:
            return
        self.nodes.append(val)

        # add a column with all zeros
        for row in self.matrix:
            row.append(0)

        # add a row with all zeros
        self.matrix.append([0] * self.getCount())
    # v1 <---> v2
    def addNodes(self,*arr):
        for i in arr:
            self.addNode(i)
    def deleteNode(self,val):
        if val not in self.nodes:
            return
        temp=self.nodes.index(val)
        # remove required row and column from matrix and nodes list 
        del self.matrix[temp]
        self.nodes.remove(val)  
    def addEdge(self, v1, v2):
        if v1 in self.nodes and v2 in self.nodes:
            indV1 = self.nodes.index(v1)
            indV2 = self.nodes.index(v2)
            self.matrix[indV1][indV2] = 1
            self.matrix[indV2][indV1] = 1
        else:
            print("One of the required node is not present")
            return
    def addEdges(self,arr:list[tuple]):
        for i ,j in arr:
            self.addEdge(i,j) 
        
    def deleteEdge(self,v1,v2):
        if v1 not in self.nodes or v2 not in self.nodes:
            print("One of the required node is not present")
            return
        indV1,indV2=self.nodes.index(v1),self.nodes.index(v2)
        self.matrix[indV1][indV2]=0
        self.matrix[indV2][indV1]=0
    
    def getCount(self) -> int:
        return len(self.nodes)

    def show(self) -> None:
        count = self.getCount()
        print("    ", end="")
        for k in range(count):
            print(f"[{self.nodes[k]}]", end=" ")
        print()
        for i in range(count):
            print(f"[{self.nodes[i]}] ", end=" ")
            for j in range(count):
                print(self.matrix[i][j], end="   ")
            print()
    def DFS(self, start, visited):
        
        print(start, end = ' ')

        visited[start] = True

        for i in range(self.v):
            
            
            if (Graph.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)


class Digraph:
    def __init__(self) -> None:
        self.nodes = []
        self.matrix = []
    def addNode(self, val) -> None:
        if val in self.nodes:
            return
        self.nodes.append(val)

        # add a column with all zeros
        for row in self.matrix:
            row.append(0)

        # add a row with all zeros
        self.matrix.append([0] * self.getCount())
    # v1 ---> v2
    def addEdge(self, v1, v2,cost=1):
        if v1 in self.nodes and v2 in self.nodes:
            indV1 = self.nodes.index(v1)
            indV2 = self.nodes.index(v2)
            self.matrix[indV1][indV2] = cost
        else:
            print("One of the required node is not present")
            return    
    def getCount(self) -> int:
        return len(self.nodes)

    def show(self) -> None:
        count = self.getCount()
        print("    ", end="")
        for k in range(count):
            print(f"[{self.nodes[k]}]", end=" ")
        print()
        for i in range(count):
            print(f"[{self.nodes[i]}] ", end=" ")
            for j in range(count):
                print(self.matrix[i][j], end="   ")
            print()
# DFS uses stack (Iterative/Recursive)
# BFS uses Queue (Iterative Only)
def DFS(graph,source):
    stack=[source]
    while len(stack)>0:
        current=stack.pop()
        print(current,end=" ")
        for neighbor in graph[current][::-1]:
            stack.append(neighbor)
def _DFS(graph,source):
    print(source)
    for i in graph[source]:
        _DFS(graph,i)
def BFS(graph,source):
    queue=[source]
    while len(queue)>0:
        current=queue.pop(0)
        print(current)
        for i in graph[current][::-1]:
            queue.append(i)


def main() -> None:
    graph={
        "a" : ["b","c"],
        "b" : ["d"],
        "c" : ["e"],
        "d" : ["f"],
        "e" : [],
        "f" : []
    }
    BFS(graph,"a")
    


if __name__ == "__main__":
    main()