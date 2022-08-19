class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.matrix = []
    def hello():
        print("hello")
    def addNode(self, val):
        if val in self.nodes:
            return
        self.nodes.append(val)

        # add a column with all zeros
        for row in self.matrix:
            row.append(0)

        # add a row with all zeros
        temp = [0]*self.getCount()
        self.matrix.append(temp)

    def getCount(self):
        return len(self.nodes)

    def show(self):
        print(self.nodes)
        for i in self.matrix:
            print(*i)


def main():
    g1 = Graph()
    g1.show()
    Graph.hello()

if __name__ == "__main__":
    main()
