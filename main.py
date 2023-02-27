import unittest
from graph import*

class GraphTest(unittest.TestCase):      

    def test_newVertexAddition(self):
        g = Graph()
        g.add(Vertex("Jure"))
        g.add(Vertex("Jure"))

        self.assertEqual(1, len(g.vertices), "Should be 1")

    def test_connection_verticesDoesNotExist(self):
        g = Graph()
        v1 = Vertex(10)
        v2 = Vertex(30)
        g.connect(v1, v2)

        self.assertFalse(v1 in g.vertices, "Vertex v1 should not exist")
        self.assertFalse(v2 in g.vertices, "Vertex v2 should not exist")

    def test_connection_verticesConnected(self):

        g = Graph()
        v1 = Vertex("Jure")
        v2 = Vertex("Stipe")
        g.add(v1)
        g.add(v2)

        g.connect(v1, v2)

        v1 = g.vertices[0]
        v2 = g.vertices[1]

        self.assertIn(v1, v2.neighbours)

if __name__ == '__main__':
    unittest.main()
    
    