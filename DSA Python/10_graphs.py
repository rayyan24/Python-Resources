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

    def addEdge(self, v1, v2,cost=1):
        if v1 in self.nodes and v2 in self.nodes:
            indV1 = self.nodes.index(v1)
            indV2 = self.nodes.index(v2)
            self.matrix[indV1][indV2] = cost
            self.matrix[indV2][indV1] = cost
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


def main() -> None:
    g1 = Graph()
    g1.addNode(1)
    g1.addNode(2)
    g1.addNode(3)
    g1.addEdge(1,1)
    g1.addEdge(2,2)
    g1.addEdge(3,3)
    g1.addEdge(1,2)
    g1.addEdge(1,3)
    g1.addEdge(1,3)
    g1.addEdge(2,3)
    g1.show()
































if __name__ == "__main__":
    main()
