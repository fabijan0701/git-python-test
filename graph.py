class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbours = []
    
    def __eq__(self, __o: object) -> bool:
        return self.data == __o.data

class Graph:

    def __init__(self):
        self.vertices = []

    def add(self, vertex: Vertex):
        if (vertex not in self.vertices):
            self.vertices.append(vertex)

    def connect(self, v1: Vertex, v2: Vertex):

        if (v1 not in self.vertices or v2 not in self.vertices):
            return
        
        i1 = self.vertices.index(v1)
        i2 = self.vertices.index(v2)

        self.vertices[i1].neighbours.append(self.vertices[i1])
        self.vertices[i2].neighbours.append(self.vertices[i2])