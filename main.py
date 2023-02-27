import unittest
from graph import*

class GraphTest(unittest.TestCase):      

    def test_newVertexAddition(self):
        g = Graph()
        g.add(Vertex("Jure"))
        g.add(Vertex("Jure"))

        self.assertEqual(1, len(g.vertices), "Should be 1")


if __name__ == '__main__':
    unittest.main()
    
    