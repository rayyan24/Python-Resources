class c2dvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __str__(self):
        return f"{self.i}i + {self.j}j"
class c3dvector(c2dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
_2dvector=c2dvector(4,5)
_3dvector=c3dvector(4,5,6)
print(_2dvector)
print(_3dvector)
