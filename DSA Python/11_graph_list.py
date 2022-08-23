class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.List = {}

    def addNode(self, val):
        if val in self.List:
            return
        self.nodes.append(val)
        self.List[val] = []

    def addEdge(self, v1, v2):
        if v1 in self.nodes and v2 in self.nodes:
            self.List[v1].append(v2)
            self.List[v2].append(v1)
        else: 
            print("One of the required node is not present")
            return

    def show(self):
        print(self.nodes)
        for i in self.List:
            print(i, self.List.get(i))
    def getCount(self):
        return len(self.nodes)





class Digraph:
    def __init__(self) -> None:
        self.nodes = []
        self.List = {}

    def addNode(self, val):
        if val in self.List:
            return
        self.nodes.append(val)
        self.List[val] = []

    def addEdge(self, v1, v2):
        if v1 in self.nodes and v2 in self.nodes:
            self.List[v1].append(v2)
        else:
            print("One of the required node is not present")
            return

    def show(self):
        print(self.nodes)
        for i in self.List:
            print(i, self.List.get(i))
    def getCount(self):
        return len(self.nodes)

def main():
    pass


if __name__ == "__main__":
    main()
